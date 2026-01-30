from aoc.core import timeit
import re


@timeit
def part1(data: str) -> int:
    pattern = re.compile(r'\\\\|\\"|\\x[0-9a-fA-F]{2}')
    total_difference = 0
    for line_string in data.strip().splitlines():
        code_chars = len(line_string)
        found_match = pattern.sub("*", line_string[1:-1])

        total_difference += code_chars - len(found_match)

    return total_difference


@timeit
def part2(data: str) -> int:
    total_difference: int = 0

    def get_encoded_length(s):
        encoded = re.sub(r'[\\"]', r"\\\g<0>", s)

        return len(encoded) + 2

    for line_string in data.strip().splitlines():
        total_difference += get_encoded_length(line_string) - len(line_string)

    return total_difference
