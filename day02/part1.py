from day02.utils import process_dimensions

def solve(lines: str) -> int:
    
    sum = 0
    # dimensions represented as length x width x height (l x w x h)
    for line in lines:
        
        l, w, h = process_dimensions(line)
        #print(l, w, h)
        lw = 2*l*w
        wh = 2*w*h
        hl = 2*h*l

        surface_area = (lw) + (wh) + (hl)
        #print(surface_area)

        smallest_side_area = min((lw), (wh), (hl)) // 2
        #print(smallest_side_area)

        sum += (smallest_side_area + surface_area)
                
    
    return sum

def day02_part1_solution(lines: str) -> int:

    #print(lines)
    return solve(lines)