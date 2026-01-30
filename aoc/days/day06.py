from aoc.core import timeit
import re
import numpy as np


# My implementation takes approx 600 ms
""" @timeit
def part1(data: str) -> int:

    light_grid: list = [[False for _ in range(1000)] for _ in range(1000)]

    moves = data.splitlines()
    for move in moves:
        move_coords = re.findall(r"(\d+),(\d+)", move)
        move_list = [x for x in move.split(" ")]

        x1: int = int(move_coords[0][0])
        y1: int = int(move_coords[0][1])
        x2: int = int(move_coords[1][0])
        y2: int = int(move_coords[1][1])

        if move_list[0] == "toggle":

            # print("Toggling")
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if light_grid[x][y] == True:
                        light_grid[x][y] = False
                    else:
                        light_grid[x][y] = True
        else:
            if move_list[1] == "on":
                # print(f"Turning On: {move}")
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        light_grid[x][y] = True
                        # a = light_grid[x][y]

            elif move_list[1] == "off":
                # print(f"Turning Off: {move}")
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        light_grid[x][y] = False
                        # a = light_grid[x][y]

    
    # return np.count_nonzero(light_grid)
    return sum(sum(row) for row in light_grid) """


# Takes 3 ms
@timeit
def part1(data: str) -> int:
    light_grid = np.zeros((1000, 1000), dtype=bool)

    for move in data.splitlines():
        x1, y1, x2, y2 = map(
            int,
            re.findall(r"(\d+),(\d+)", move)[0] + re.findall(r"(\d+),(\d+)", move)[1],
        )

        if move.startswith("toggle"):
            light_grid[x1 : x2 + 1, y1 : y2 + 1] ^= True
        elif "turn on" in move:
            light_grid[x1 : x2 + 1, y1 : y2 + 1] = True
        else:
            light_grid[x1 : x2 + 1, y1 : y2 + 1] = False

    return light_grid.sum()


@timeit
def part2(data: str) -> int:
    light_grid: list = [[0 for _ in range(1000)] for _ in range(1000)]

    for move in data.splitlines():
        x1, y1, x2, y2 = map(
            int,
            re.findall(r"(\d+),(\d+)", move)[0] + re.findall(r"(\d+),(\d+)", move)[1],
        )

        if move.startswith("toggle"):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    light_grid[x][y] += 2

        elif "turn on" in move:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    light_grid[x][y] += 1

        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if light_grid[x][y] > 0:
                        light_grid[x][y] -= 1
                    else:
                        pass
    return sum(sum(row) for row in light_grid)
