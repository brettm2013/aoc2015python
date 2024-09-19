from Common.utils import read_lines_from_file

from day02.part1 import day02_part1_solution
from day02.part2 import day02_part2_solution



data_file_name = 'day02.txt'

print("Part 1 Result:", day02_part1_solution(read_lines_from_file(data_file_name)))
print("Part 2 Result:", day02_part2_solution(read_lines_from_file(data_file_name)))