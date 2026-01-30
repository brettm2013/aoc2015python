import importlib
import sys
from aoc.core import load_input


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m aoc.runner <day>")
        return

    day = int(sys.argv[1])
    module = importlib.import_module((f"aoc.days.day{day:02d}"))

    data = load_input(day)

    p1, t1 = module.part1(data)
    p2, t2 = module.part2(data)

    print(f"Day {day:02d}")
    print(f"  Part 1: {p1}  ({t1:.2f} ms)")
    print(f"  Part 2: {p2}  ({t2:.2f} ms)")


if __name__ == "__main__":
    main()
