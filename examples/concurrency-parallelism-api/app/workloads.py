"""Funciones de trabajo que deben poder importarse desde procesos hijos."""

from os import getpid


def cpu_work(task_id: int, iterations: int) -> dict[str, int]:
    """Ejecuta trabajo puro de Python y devuelve el PID que lo procesó.

    Al ser una función de nivel de módulo, ProcessPoolExecutor puede serializarla
    y ejecutarla en otro intérprete de Python, evitando la limitación del GIL.
    """
    checksum = 0
    for number in range(iterations):
        checksum = (checksum + number * number) % 1_000_000_007

    return {
        "task_id": task_id,
        "pid": getpid(),
        "checksum": checksum,
    }
