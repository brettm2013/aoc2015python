from aoc.core import timeit
import re


@timeit
def part1(data: str) -> int:
    match_vowel: re.Pattern = re.compile(r"[aeiou]")
    match_repeat: re.Pattern = re.compile(r"(.)\1+")
    match_badpairs: re.Pattern = re.compile(r"(ab|cd|pq|xy)")

    good_words: int = 0
    for word in data.splitlines():
        good: bool = True
        if len(match_vowel.findall(word)) < 3:
            good = False
        if len(match_repeat.findall(word)) < 1:
            good = False
        if len(match_badpairs.findall(word)) > 0:
            good = False

        if good:
            # print(word)
            good_words += 1

    return good_words


@timeit
def part2(data: str) -> int:
    match_pair: re.Pattern = re.compile(r"(..).*\1")
    match_repeat: re.Pattern = re.compile(r"(.).\1")

    good_words: int = 0
    for word in data.splitlines():
        good: bool = False
        if len(match_pair.findall(word)) > 0:
            if len(match_repeat.findall(word)) > 0:
                good = True

        if good:
            #         print(word)
            good_words += 1

    return good_words
