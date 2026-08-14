# Algoritmos de entrevistas en Python

Este módulo es un espacio separado del recorrido de los 100 días. La idea no es
memorizar soluciones: es practicar una forma repetible de pensar, reconocer
patrones y, al mismo tiempo, aprender el Python necesario para expresarlos.

## El proceso que usaremos

Antes de escribir código, seguí estos cinco pasos:

1. **Entender:** reformulá el problema, identificá entradas, salida y restricciones.
2. **Explorar ejemplos:** incluí casos simples, complejos, vacíos e inválidos.
3. **Descomponer:** escribí en lenguaje natural los pasos de la solución.
4. **Resolver o simplificar:** empezá por una solución correcta; si te trabás,
   aislá la parte difícil y resolvé una versión más simple.
5. **Revisar y refactorizar:** verificá el resultado, la legibilidad y las
   complejidades temporal y espacial.

En una entrevista conviene decir estos pasos en voz alta. El entrevistador no
solo evalúa el resultado: también necesita entender cómo llegaste a él.

## Contenido actual

| Patrón | Pregunta que ayuda a reconocerlo | Ejercicios |
|---|---|---|
| Contador de frecuencias | ¿Necesito comparar cantidades de valores? | cuadrados correspondientes, anagramas |
| Dos punteros | ¿Los datos ordenados permiten descartar extremos? | suma cero, valores únicos |
| Ventana deslizante | ¿Busco algo en un segmento contiguo? | suma máxima de `k` elementos |
| Dividir y conquistar | ¿Puedo descartar la mitad en cada paso? | búsqueda binaria |

Cada archivo contiene:

- el enunciado y las decisiones importantes;
- una solución ingenua para usar como punto de partida;
- una solución optimizada;
- complejidad temporal y espacial;
- ejemplos ejecutables mediante tests.

## Cómo estudiar un ejercicio

Tomá, por ejemplo, `sum_zero`:

1. Leé únicamente el enunciado en `two_pointers.py`.
2. Escribí tres casos a mano, incluyendo uno sin solución.
3. Implementá primero dos bucles anidados sin mirar la solución.
4. Preguntate qué permite descartar el hecho de que la lista esté ordenada.
5. Compará tu idea con `sum_zero` y explicá por qué mover cada puntero es seguro.
6. Corré los tests y agregá un caso que no estuviera contemplado.

## Python que aparece en las soluciones

- `list[int]`, `tuple[int, int] | None`: anotaciones de tipos.
- `dict.get(clave, 0)`: lectura de un contador con valor inicial.
- `collections.Counter`: contador de frecuencias de la biblioteca estándar.
- `enumerate`: recorrer valores junto con su índice.
- cortes como `values[:window_size]`: obtener una porción de una lista.
- `raise ValueError(...)`: rechazar argumentos cuyo significado sería ambiguo.

Las anotaciones ayudan a documentar, pero Python no las valida automáticamente
al ejecutar. Los tests son los que comprueban el comportamiento.

## Ejecutar todo

Desde la raíz del repositorio:

```sh
python3 -m unittest discover -s interview_algorithms/tests -v
```

También podés abrir cualquier archivo de `problems/` y ejecutar sus ejemplos:

```sh
python3 -m interview_algorithms.problems.two_pointers
```

## Agregar el próximo problema

Copiá `problem_template.py`, renombralo con `snake_case` y completá cada sección.
Luego agregá sus casos en `tests/`. Una buena progresión desde acá sería:

1. frecuencia: `same_frequency` y `are_there_duplicates`;
2. dos punteros: `average_pair` y eliminación de duplicados;
3. ventana: substring más largo sin caracteres repetidos;
4. recursión, ordenamiento y estructuras de datos;
5. backtracking y programación dinámica.

El objetivo de cada incorporación es poder explicar no solo **qué** funciona,
sino **por qué** y bajo qué restricciones.

