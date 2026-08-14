"""Patrón: contador de frecuencias.

Es útil cuando importa cuántas veces aparece cada valor. Cambiar búsquedas
repetidas por uno o dos diccionarios suele reducir O(n²) a O(n).
"""

from collections import Counter


def same_squared_naive(first: list[int], second: list[int]) -> bool:
    """Indica si ``second`` contiene los cuadrados de ``first``.

    La frecuencia debe coincidir. Esta versión copia la segunda lista y busca
    cada cuadrado en ella: O(n²) en tiempo y O(n) en espacio.
    """
    if len(first) != len(second):
        return False

    remaining = second.copy()
    for value in first:
        squared = value**2
        if squared not in remaining:
            return False
        remaining.remove(squared)
    return True


def same_squared(first: list[int], second: list[int]) -> bool:
    """Resuelve el mismo problema con contadores: O(n) tiempo y O(n) espacio."""
    if len(first) != len(second):
        return False

    squared_frequencies = Counter(value**2 for value in first)
    return squared_frequencies == Counter(second)


def valid_anagram(first: str, second: str) -> bool:
    """Indica si dos strings contienen exactamente los mismos caracteres.

    Se distingue entre mayúsculas y minúsculas y se tienen en cuenta espacios
    y signos. Complejidad: O(n) tiempo y O(k) espacio, donde k es la cantidad
    de caracteres distintos.
    """
    if len(first) != len(second):
        return False

    frequencies: dict[str, int] = {}
    for character in first:
        frequencies[character] = frequencies.get(character, 0) + 1

    for character in second:
        if frequencies.get(character, 0) == 0:
            return False
        frequencies[character] -= 1
    return True


if __name__ == "__main__":
    assert same_squared([1, 2, 3], [4, 1, 10])
    assert not same_squared([1, 2, 1], [4, 4, 1])
    assert valid_anagram("anagram", "nagaram")
    print("Ejemplos de contador de frecuencias: OK")
