"""Patrón: ventana deslizante para segmentos contiguos."""


def max_subarray_sum_naive(values: list[int], window_size: int) -> int | None:
    """Obtiene la suma máxima recalculando cada ventana: O(n*k) tiempo."""
    _validate_window_size(window_size)
    if window_size > len(values):
        return None

    return max(
        sum(values[start : start + window_size])
        for start in range(len(values) - window_size + 1)
    )


def max_subarray_sum(values: list[int], window_size: int) -> int | None:
    """Obtiene la suma máxima de ``window_size`` elementos consecutivos.

    Al avanzar se resta el elemento que sale y se suma el que entra, evitando
    recalcular toda la ventana. Complejidad: O(n) tiempo y O(1) espacio.
    """
    _validate_window_size(window_size)
    if window_size > len(values):
        return None

    current_sum = sum(values[:window_size])
    maximum_sum = current_sum

    for entering_index in range(window_size, len(values)):
        leaving_index = entering_index - window_size
        current_sum += values[entering_index] - values[leaving_index]
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum


def _validate_window_size(window_size: int) -> None:
    if window_size <= 0:
        raise ValueError("window_size debe ser mayor que cero")


if __name__ == "__main__":
    assert max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 2) == 10
    assert max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 4) == 17
    assert max_subarray_sum([], 4) is None
    print("Ejemplos de ventana deslizante: OK")

