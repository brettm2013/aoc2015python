from aoc.core import timeit
import math


@timeit
def part1(data: str) -> int:
    # print(data)
    #

    boxes: list = [line for line in data.split("\n")]
    wrapping_paper = 0

    for box in boxes:
        dims: list = [int(dim) for dim in box.split("x")]

        length: int = dims[0]
        width: int = dims[1]
        height: int = dims[2]
        # print(f"length: {length}, width: {width}, Height: {height}")

        # Surface area of box 2*l*w + 2*w*h + 2*h*l
        # Factored down into 2 * ((l*w) + (w*h) + (h*l))
        surface_area: int = 2 * (
            (length * width) + (width * height) + (length * height)
        )
        # Remove largest side and multiply each element together
        dims.remove(max(dims))
        smallest_side_area: int = math.prod(dims)
        # smallest_side_area: int = dims[0] * dims[1]
        wrapping_paper += surface_area + smallest_side_area

    return wrapping_paper


@timeit
def part2(data: str) -> int:
    boxes: list = [line for line in data.split("\n")]
    ribbon: int = 0

    for box in boxes:
        dims: list = [int(dim) for dim in box.split("x")]
        volume: int = math.prod(dims)
        dims.remove(max(dims))
        permiter = 2 * (dims[0] + dims[1])
        ribbon += volume + permiter

    return ribbon
