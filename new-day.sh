#!/usr/bin/env bash
# Creates the directory for a new course day.
# Usage: ./new-day.sh 11 "while-loops-fizzbuzz"
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "Usage: $0 <day-number> <topic-slug>" >&2
  echo "Example: $0 11 while-loops-fizzbuzz" >&2
  exit 1
fi

num=$(printf "%02d" "$1")
slug=$(echo "$2" | tr '[:upper:] ' '[:lower:]-')
dir="$(dirname "$0")/days/day-${num}-${slug}"

if [ -d "$dir" ]; then
  echo "Already exists: $dir" >&2
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

## Concepts

-

## Project

-

## Questions

-
EOF

echo "Created: $dir"
