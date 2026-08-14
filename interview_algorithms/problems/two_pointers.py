"""Patrón: dos punteros sobre datos ordenados.

El orden permite descartar candidatos sin examinarlos uno por uno. Antes de
usar este patrón hay que confirmar que la entrada realmente está ordenada.
"""


def sum_zero_naive(values: list[int]) -> tuple[int, int] | None:
    """Devuelve el primer par que suma cero usando O(n²) tiempo y O(1) espacio."""
    for left_index, left_value in enumerate(values):
        for right_index in range(left_index + 1, len(values)):
            right_value = values[right_index]
            if left_value + right_value == 0:
                return left_value, right_value
    return None


def sum_zero(values: list[int]) -> tuple[int, int] | None:
    """Devuelve un par que suma cero en una lista ordenada.

    Si la suma es positiva, ningún valor a la derecha puede mejorarla: se mueve
    el puntero derecho. Si es negativa, se mueve el izquierdo.
    Complejidad: O(n) tiempo y O(1) espacio.
    """
    left = 0
    right = len(values) - 1

    while left < right:
        current_sum = values[left] + values[right]
        if current_sum == 0:
            return values[left], values[right]
        if current_sum > 0:
            right -= 1
        else:
            left += 1
    return None


def count_unique_values(values: list[int]) -> int:
    """Cuenta valores distintos en una lista ordenada: O(n) tiempo, O(1) espacio."""
    if not values:
        return 0

    unique_count = 1
    previous = values[0]
    for index in range(1, len(values)):
        current = values[index]
        if current != previous:
            unique_count += 1
            previous = current
    return unique_count


if __name__ == "__main__":
    assert sum_zero([-3, -2, -1, 0, 1, 2, 3]) == (-3, 3)
    assert sum_zero([-2, 0, 1, 3]) is None
    assert count_unique_values([-2, -1, -1, 0, 1]) == 4
    print("Ejemplos de dos punteros: OK")
