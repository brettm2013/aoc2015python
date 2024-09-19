def solve(lines: str) -> int:
    
    sum = 0
    step = 0
    for line in lines:
        for char in line:
            #print(char)
            step += 1
            match char: 

                case '(':
                    sum += 1
                case ')':
                    sum -= 1
                case _:
                    print("Error, did not recognize")

            if sum < 0:
                return step
                
    return 0

def day01_part2_solution(lines) -> int:

    #print(lines)
    return solve(lines)