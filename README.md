# 100 Days of Code — The Complete Python Pro Bootcamp

Code and projects from Angela Yu's 100-day Python Udemy course (57 hours).

## Structure

```
100-days-of-python/
├── days/
│   ├── day-01-variables/
│   │   ├── main.py          # daily exercise or project
│   │   └── NOTES.md         # notes and new concepts
│   └── ...
├── new-day.sh               # creates the next day's directory
├── requirements.txt         # dependencies (added as needed)
└── .venv/                   # virtual environment (not tracked)
```

## Setup

```sh
cd ~/Documents/codes/100-days-of-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Create a new day

```sh
./new-day.sh 11 "while-loops-fizzbuzz"
```

This creates `days/day-11-while-loops-fizzbuzz/` with `main.py` and `NOTES.md`.

## Run an exercise

```sh
python days/day-01-variables/main.py
```

## Additional examples

- [Concurrency vs. parallelism with FastAPI](examples/concurrency-parallelism-api/README.md)
- [Coding interview algorithms in Python](interview_algorithms/README.md)

## Progress

| Day | Topic | Project | Status |
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

Mark each day with ✅ as you progress.
