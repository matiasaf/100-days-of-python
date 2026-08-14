"""Workload functions that must be importable by child processes."""

from os import getpid


def cpu_work(task_id: int, iterations: int) -> dict[str, int]:
    """Run pure Python work and return the PID that processed it.

    Because this is a module-level function, ProcessPoolExecutor can serialize
    it and run it in another Python interpreter, bypassing the GIL limitation.
    """
    checksum = 0
    for number in range(iterations):
        checksum = (checksum + number * number) % 1_000_000_007

    return {
        "task_id": task_id,
        "pid": getpid(),
        "checksum": checksum,
    }
