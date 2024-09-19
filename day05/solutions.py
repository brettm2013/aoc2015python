from Common.utils import read_lines_from_file

from day05.part1 import day05_part1_solution
from day05.part2 import day05_part2_solution


data_file_name = 'day05.txt'

print("Part 1 Result:", day05_part1_solution(read_lines_from_file(data_file_name)))
print("Part 2 Result:", day05_part2_solution(read_lines_from_file(data_file_name)))