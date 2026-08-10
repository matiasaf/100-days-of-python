import httpx
import pytest

from app.main import app
from app.workloads import cpu_work

pytestmark = pytest.mark.anyio


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as value:
        yield value


async def test_root_lists_both_experiments(client: httpx.AsyncClient) -> None:
    response = await client.get("/")

    assert response.status_code == 200
    assert set(response.json()["experiments"]) == {"concurrency", "parallelism"}


async def test_concurrent_io_overlaps_waits(client: httpx.AsyncClient) -> None:
    response = await client.get(
        "/demo/concurrency", params={"tasks": 3, "delay": 0.03}
    )

    assert response.status_code == 200
    body = response.json()
    assert body["concept"] == "concurrency"
    assert body["concurrent"]["elapsed_ms"] < body["sequential"]["elapsed_ms"]
    starts = [item["started_at_ms"] for item in body["concurrent"]["timeline"]]
    assert max(starts) < 20


async def test_parallel_endpoint_returns_process_results(
    client: httpx.AsyncClient,
) -> None:
    response = await client.get(
        "/demo/parallelism",
        params={"tasks": 2, "iterations": 10_000},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["concept"] == "parallelism"
    assert len(body["sequential"]["results"]) == 2
    assert len(body["parallel"]["results"]) == 2
    assert body["parallel_workers"] >= 1


def test_cpu_work_is_deterministic() -> None:
    first = cpu_work(task_id=1, iterations=100)
    second = cpu_work(task_id=1, iterations=100)

    assert first["checksum"] == second["checksum"]
