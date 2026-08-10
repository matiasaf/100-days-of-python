"""API para observar la diferencia entre concurrencia y paralelismo."""

import asyncio
from concurrent.futures import ProcessPoolExecutor
from os import cpu_count, getpid
from time import perf_counter
from typing import Annotated, Literal

from fastapi import FastAPI, Query

from app.workloads import cpu_work

app = FastAPI(
    title="Concurrencia vs. paralelismo",
    description=(
        "Experimentos reproducibles: asyncio para esperas de I/O y procesos "
        "separados para trabajo intensivo de CPU."
    ),
    version="1.0.0",
)


def milliseconds(seconds: float) -> float:
    return round(seconds * 1_000, 2)


async def simulated_io(task_id: int, delay: float, origin: float) -> dict:
    """Representa una consulta a una API, base de datos o archivo."""
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
    """Ejecuta CPU fuera del proceso de FastAPI para no bloquear su event loop."""
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
        "message": "Abrí /docs y ejecutá los dos experimentos.",
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
    """Compara esperas secuenciales con esperas concurrentes en un solo proceso."""
    sequential = await run_io_batch(tasks, delay, concurrent=False)
    concurrent = await run_io_batch(tasks, delay, concurrent=True)

    return {
        "concept": "concurrency",
        "kind_of_work": "I/O-bound (simulated)",
        "process_pid": getpid(),
        "expected": {
            "sequential_ms": f"aproximadamente {tasks * delay * 1_000:.0f}",
            "concurrent_ms": f"aproximadamente {delay * 1_000:.0f}",
        },
        "sequential": sequential,
        "concurrent": concurrent,
        "speedup": round(sequential["elapsed_ms"] / concurrent["elapsed_ms"], 2),
        "explanation": (
            "Las tareas concurrentes comparten un event loop: cuando una espera, "
            "otra puede avanzar. No hace falta ejecutar Python en varios núcleos."
        ),
    }


@app.get("/demo/parallelism", tags=["experiments"])
async def parallelism_demo(
    tasks: Annotated[int, Query(ge=2, le=8)] = 4,
    iterations: Annotated[int, Query(ge=10_000, le=20_000_000)] = 2_000_000,
) -> dict:
    """Compara trabajo de CPU en uno y en varios procesos."""
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
            "Cada PID identifica un intérprete separado. Con varios núcleos, esos "
            "procesos pueden calcular al mismo tiempo y no compiten por el GIL."
        ),
        "caveat": (
            "Para trabajos pequeños, crear procesos puede costar más que la mejora "
            "obtenida; aumentá iterations para que la diferencia sea visible."
        ),
    }
