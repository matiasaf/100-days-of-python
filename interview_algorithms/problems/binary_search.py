"""Patrón: dividir y conquistar mediante búsqueda binaria."""


def linear_search(values: list[int], target: int) -> int:
    """Busca de izquierda a derecha: O(n) tiempo y O(1) espacio."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Busca ``target`` en una lista ordenada: O(log n) tiempo, O(1) espacio.

    La comparación con el elemento central permite descartar la mitad que no
    puede contener al objetivo. Devuelve -1 cuando el valor no está presente.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        current = values[middle]

        if current == target:
            return middle
        if current < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6], 11) == -1
    print("Ejemplos de búsqueda: OK")
