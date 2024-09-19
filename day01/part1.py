def solve(lines: str) -> int:
    
    sum = 0
    for line in lines:
        for char in line:
            #print(char)
            match char: 

                case '(':
                    sum += 1
                case ')':
                    sum -= 1
                case _:
                    print("Error, did not recognize")
                
    
    return sum

def day01_part1_solution(lines: str) -> int:

    #print(lines)
    return solve(lines)