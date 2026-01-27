from aoc.core import timeit
import hashlib


@timeit
def part1(data: str) -> int:
    start = 0
    hash_input = data

    while True:
        start += 1
        hash_input = data + str(start)
        outcome_string = hashlib.md5(hash_input.encode()).hexdigest()

        # print(outcome_string)

        if (
            outcome_string[0] == "0"
            and outcome_string[1] == "0"
            and outcome_string[2] == "0"
            and outcome_string[3] == "0"
            and outcome_string[4] == "0"
        ):
            break
    return start


@timeit
def part2(data: str) -> int:
    start = 0
    hash_input = data

    while True:
        start += 1
        hash_input = data + str(start)
        outcome_string = hashlib.md5(hash_input.encode()).hexdigest()

        if outcome_string[0] != "0":
            continue
        if outcome_string[1] != "0":
            continue
        if outcome_string[2] != "0":
            continue
        if outcome_string[3] != "0":
            continue
        if outcome_string[4] != "0":
            continue
        if outcome_string[5] != "0":
            continue
        break
    return start
