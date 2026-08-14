# Concurrency vs. Parallelism with FastAPI

This example applies the ideas from a
[freeCodeCamp article](https://www.freecodecamp.org/news/concurrency-vs-parallelism-whats-the-difference-and-why-should-you-care/)
to an API:

- **Concurrency:** organizing several tasks so they make progress during the
  same period. It is especially useful while a program waits for I/O.
- **Parallelism:** running computations at the same time using multiple cores
  or processors. It is useful for CPU-intensive work.

## Run the API

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd examples/concurrency-parallelism-api
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000/docs> to try the endpoints in Swagger UI.

## Experiment 1: concurrency

```bash
curl "http://127.0.0.1:8000/demo/concurrency?tasks=4&delay=0.25"
```

The API simulates four 250 ms I/O operations. They should take about 1,000 ms
sequentially and about 250 ms with `asyncio.gather`. All operations run under
the same PID: they overlap while waiting, but Python bytecode is not processed
in parallel.

## Experiment 2: parallelism

```bash
curl "http://127.0.0.1:8000/demo/parallelism?tasks=4&iterations=2000000"
```

The API runs the same computation first with one worker and then with up to four
processes. The `worker_pids` list shows the distinct processes. The actual
speedup depends on the available cores and the cost of creating processes. For
very small workloads, the parallel version may even be slower.

Computations are sent to `ProcessPoolExecutor` without blocking the event loop,
so FastAPI can continue serving other requests while it waits for the result.

## Run the tests

```bash
cd examples/concurrency-parallelism-api
pytest -q
```

## Which approach should you use?

| Workload | Examples | Tool used here |
|---|---|---|
| I/O-bound | HTTP, databases, files | `async`/`await` + `asyncio.gather` |
| CPU-bound | computations, images, compression | `ProcessPoolExecutor` |

In CPython, threads do not guarantee parallelism for these computations because
of the GIL. Separate processes can execute bytecode on different cores.
