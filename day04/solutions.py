from Common.utils import read_lines_from_file

from day04.part1 import day04_part1_solution
from day04.part2 import day04_part2_solution


data_file_name = 'day04.txt'

print("Part 1 Result:", day04_part1_solution(read_lines_from_file(data_file_name)))
print("Part 2 Result:", day04_part2_solution(read_lines_from_file(data_file_name)))