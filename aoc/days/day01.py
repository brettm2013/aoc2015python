from aoc.core import timeit


@timeit
def part1(data: str) -> int:
    total: int = 0
    for move in data:
        if move == "(":
            total += 1
        elif move == ")":
            total -= 1
    return total


@timeit
def part2(data: str) -> int:
    total: int = 0
    move_num: int = 0
    for move in data:
        move_num += 1
        if move == "(":
            total += 1
        elif move == ")":
            total -= 1
        if total < 0:
            break
    return move_num
