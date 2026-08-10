#!/usr/bin/env bash
# Crea la carpeta de un día nuevo del curso.
# Uso: ./new-day.sh 11 "while-loops-fizzbuzz"
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Uso: $0 <numero-de-dia> <slug-del-tema>" >&2
  echo "Ej:  $0 11 while-loops-fizzbuzz" >&2
  exit 1
fi

num=$(printf "%02d" "$1")
slug=$(echo "$2" | tr '[:upper:] ' '[:lower:]-')
dir="$(dirname "$0")/days/day-${num}-${slug}"

if [ -d "$dir" ]; then
  echo "Ya existe: $dir" >&2
  exit 1
fi

mkdir -p "$dir"

cat > "$dir/main.py" <<EOF
"""Day ${num} — ${2}"""


def main() -> None:
    print("Day ${num}")


if __name__ == "__main__":
    main()
EOF

cat > "$dir/NOTES.md" <<EOF
# Day ${num} — ${2}

## Conceptos

-

## Proyecto

-

## Dudas

-
EOF

echo "Creado: $dir"
