"""API for observing the difference between concurrency and parallelism."""

import asyncio
from concurrent.futures import ProcessPoolExecutor
from os import cpu_count, getpid
from time import perf_counter
from typing import Annotated, Literal

from fastapi import FastAPI, Query

from app.workloads import cpu_work

app = FastAPI(
    title="Concurrency vs. Parallelism",
    description=(
        "Reproducible experiments: asyncio for I/O waits and separate "
        "processes for CPU-intensive work."
    ),
    version="1.0.0",
)


def milliseconds(seconds: float) -> float:
    return round(seconds * 1_000, 2)


async def simulated_io(task_id: int, delay: float, origin: float) -> dict:
    """Represent a request to an API, database, or file."""
    started = perf_counter()
    await asyncio.sleep(delay)
    finished = perf_counter()
    return {
        "task_id": task_id,
        "started_at_ms": milliseconds(started - origin),
        "finished_at_ms": milliseconds(finished - origin),
    }


async def run_io_batch(tasks: int, delay: float, concurrent: bool) -> dict:
    origin = perf_counter()

    if concurrent:
        results = await asyncio.gather(
            *(simulated_io(task_id, delay, origin) for task_id in range(tasks))
        )
    else:
        results = []
        for task_id in range(tasks):
            results.append(await simulated_io(task_id, delay, origin))

    return {
        "elapsed_ms": milliseconds(perf_counter() - origin),
        "timeline": results,
    }


async def run_cpu_batch(tasks: int, iterations: int, workers: int) -> dict:
    """Run CPU work outside FastAPI's process to avoid blocking its event loop."""
    origin = perf_counter()
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [
            loop.run_in_executor(executor, cpu_work, task_id, iterations)
            for task_id in range(tasks)
        ]
        results = await asyncio.gather(*futures)

    return {
        "elapsed_ms": milliseconds(perf_counter() - origin),
        "worker_pids": sorted({result["pid"] for result in results}),
        "results": results,
    }


@app.get("/", tags=["info"])
async def root() -> dict:
    return {
        "message": "Open /docs and run both experiments.",
        "experiments": {
            "concurrency": "/demo/concurrency?tasks=4&delay=0.25",
            "parallelism": "/demo/parallelism?tasks=4&iterations=2000000",
        },
    }


@app.get("/health", tags=["info"])
async def health() -> dict[str, Literal["ok"]]:
    return {"status": "ok"}


@app.get("/demo/concurrency", tags=["experiments"])
async def concurrency_demo(
    tasks: Annotated[int, Query(ge=2, le=20)] = 4,
    delay: Annotated[float, Query(gt=0, le=2)] = 0.25,
) -> dict:
    """Compare sequential and concurrent waits within a single process."""
    sequential = await run_io_batch(tasks, delay, concurrent=False)
    concurrent = await run_io_batch(tasks, delay, concurrent=True)

    return {
        "concept": "concurrency",
        "kind_of_work": "I/O-bound (simulated)",
        "process_pid": getpid(),
        "expected": {
            "sequential_ms": f"approximately {tasks * delay * 1_000:.0f}",
            "concurrent_ms": f"approximately {delay * 1_000:.0f}",
        },
        "sequential": sequential,
        "concurrent": concurrent,
        "speedup": round(sequential["elapsed_ms"] / concurrent["elapsed_ms"], 2),
        "explanation": (
            "Concurrent tasks share an event loop: while one waits, another can "
            "make progress. Python does not need to run on multiple cores."
        ),
    }


@app.get("/demo/parallelism", tags=["experiments"])
async def parallelism_demo(
    tasks: Annotated[int, Query(ge=2, le=8)] = 4,
    iterations: Annotated[int, Query(ge=10_000, le=20_000_000)] = 2_000_000,
) -> dict:
    """Compare CPU work in one process and across multiple processes."""
    available_cpus = cpu_count() or 1
    parallel_workers = min(tasks, available_cpus)

    sequential = await run_cpu_batch(tasks, iterations, workers=1)
    parallel = await run_cpu_batch(tasks, iterations, workers=parallel_workers)

    return {
        "concept": "parallelism",
        "kind_of_work": "CPU-bound",
        "api_process_pid": getpid(),
        "available_cpus": available_cpus,
        "parallel_workers": parallel_workers,
        "sequential": sequential,
        "parallel": parallel,
        "speedup": round(sequential["elapsed_ms"] / parallel["elapsed_ms"], 2),
        "explanation": (
            "Each PID identifies a separate interpreter. With multiple cores, "
            "these processes can compute simultaneously without competing for "
            "the GIL."
        ),
        "caveat": (
            "For small workloads, creating processes can cost more than the "
            "resulting improvement. Increase iterations to make the difference "
            "visible."
        ),
    }
