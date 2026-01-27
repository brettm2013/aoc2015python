from aoc.core import timeit
import re


@timeit
def part1(data: str) -> int:
    light_grid: list = [[False for _ in range(1000)] for _ in range(1000)]

    # match_moves: re.Pattern = re.compile(r"(d\+),(\d+)")
    moves = data.splitlines()
    for move in moves:
        # move_coords = match_moves.findall(move)
        move_coords = re.findall(r"(\d+),(\d+)", move)
        # move_coords_list = [(int(a), int(b)) for a, b in move_coords]
        move_list = [x for x in move.split(" ")]

        if move_list[0] == "toggle":
            print(f"Toggling: {move}")
            print(f"MOVES: {move_coords}")
        else:
            if move_list[1] == "on":
                print(f"Turning On: {move}")
            elif move_list[1] == "off":
                print(f"Turning Off: {move}")

    return 0


@timeit
def part2(data: str) -> int:
    return 0
