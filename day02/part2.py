from day02.utils import process_dimensions

def solve(lines: str) -> int:
    
    ribbon_length = 0
    for line in lines:
        l, w, h = process_dimensions(line)
        #print(l, w, h)
        volume = (l*w*h)

        # Make into a list so we can remove the largest side and calculate 
        # smallest perimeter 
        side_list = [l, w, h] 
        largest_side = max(side_list)
        side_list.remove(largest_side)
        smallest_perimeter = ((2*side_list[0]) + (2*side_list[1]))

        ribbon_length += (volume + smallest_perimeter)


    return ribbon_length

def day02_part2_solution(lines) -> int:

    #print(lines)
    return solve(lines)