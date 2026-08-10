# 100 Days of Code — The Complete Python Pro Bootcamp

Código y proyectos del curso de Udemy (Angela Yu, 57 h · 100 días).

## Estructura

```
100-days-of-python/
├── days/
│   ├── day-01-variables/
│   │   ├── main.py          # ejercicio / proyecto del día
│   │   └── NOTES.md         # apuntes y conceptos nuevos
│   └── ...
├── new-day.sh               # crea la carpeta del próximo día
├── requirements.txt         # dependencias (se van sumando)
└── .venv/                   # entorno virtual (no se versiona)
```

## Setup

```sh
cd ~/Documents/codes/100-days-of-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Crear un día nuevo

```sh
./new-day.sh 11 "while-loops-fizzbuzz"
```

Crea `days/day-11-while-loops-fizzbuzz/` con `main.py` y `NOTES.md`.

## Correr un ejercicio

```sh
python days/day-01-variables/main.py
```

## Ejemplos adicionales

- [Concurrencia vs. paralelismo con FastAPI](examples/concurrency-parallelism-api/README.md)

## Progreso

| Día | Tema | Proyecto | Estado |
|-----|------|----------|--------|
| 01 | Variables | Band Name Generator | ⬜ |
| 02 | Data Types & Strings | Tip Calculator | ⬜ |
| 03 | Control Flow & Logical Operators | Treasure Island | ⬜ |
| 04 | Randomisation & Lists | Rock Paper Scissors | ⬜ |
| 05 | Loops | Password Generator | ⬜ |
| 06 | Functions & Karel | Reeborg's World | ⬜ |
| 07 | Hangman | Hangman | ⬜ |
| 08 | Function Parameters | Caesar Cipher | ⬜ |
| 09 | Dictionaries & Nesting | Secret Auction | ⬜ |
| 10 | Functions with Outputs | Calculator | ⬜ |

Marcá con ✅ a medida que avanzás.
