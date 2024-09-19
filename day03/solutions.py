from Common.utils import read_lines_from_file

from day03.part1 import day03_part1_solution
from day03.part2 import day03_part2_solution



data_file_name = 'day03.txt'

print("Part 1 Result:", day03_part1_solution(read_lines_from_file(data_file_name)))
print("Part 2 Result:", day03_part2_solution(read_lines_from_file(data_file_name)))