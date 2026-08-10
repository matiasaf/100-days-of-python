# Concurrencia vs. paralelismo con FastAPI

Este ejemplo lleva a una API las ideas del artículo de
[freeCodeCamp](https://www.freecodecamp.org/news/concurrency-vs-parallelism-whats-the-difference-and-why-should-you-care/):

- **Concurrencia:** organizar varias tareas para que progresen durante el mismo
  período. Es especialmente útil cuando el programa espera I/O.
- **Paralelismo:** ejecutar cálculos realmente al mismo tiempo usando varios
  núcleos o procesadores. Es útil para trabajo intensivo de CPU.

## Ejecutar

Desde la raíz del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd examples/concurrency-parallelism-api
uvicorn app.main:app --reload
```

Abrí <http://127.0.0.1:8000/docs> para probar los endpoints desde Swagger UI.

## Experimento 1: concurrencia

```bash
curl "http://127.0.0.1:8000/demo/concurrency?tasks=4&delay=0.25"
```

La API simula cuatro operaciones de I/O de 250 ms. Secuencialmente deberían
demorar cerca de 1000 ms; con `asyncio.gather`, cerca de 250 ms. Todas ocurren
en el mismo PID: hay solapamiento durante la espera, no procesamiento paralelo
de bytecode de Python.

## Experimento 2: paralelismo

```bash
curl "http://127.0.0.1:8000/demo/parallelism?tasks=4&iterations=2000000"
```

La API ejecuta el mismo cálculo primero con un solo worker y luego con hasta
cuatro procesos. La lista `worker_pids` permite observar los procesos distintos.
El speedup real depende de los núcleos disponibles y del costo de crear procesos.
Para un trabajo demasiado pequeño, el paralelo incluso puede ser más lento.

Los cálculos se envían a `ProcessPoolExecutor` sin bloquear el event loop. Así,
FastAPI puede seguir atendiendo otras solicitudes mientras espera el resultado.

## Ejecutar las pruebas

```bash
cd examples/concurrency-parallelism-api
pytest -q
```

## Qué conviene usar

| Tipo de trabajo | Ejemplos | Herramienta usada aquí |
|---|---|---|
| I/O-bound | HTTP, base de datos, archivos | `async`/`await` + `asyncio.gather` |
| CPU-bound | cálculos, imágenes, compresión | `ProcessPoolExecutor` |

En CPython, usar threads para estos cálculos no garantiza paralelismo por el
GIL. Procesos separados sí pueden ejecutar bytecode en distintos núcleos.
