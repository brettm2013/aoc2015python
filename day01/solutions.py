from Common.utils import read_lines_from_file

from day01.part1 import day01_part1_solution
from day01.part2 import day01_part2_solution

data_file_name = 'day01.txt'

print("Part 1 Result:", day01_part1_solution(read_lines_from_file(data_file_name)))
print("Part 2 Result:", day01_part2_solution(read_lines_from_file(data_file_name)))