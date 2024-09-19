def solve(lines: str) -> int:
    
    start = (0,0)
    visit_counts = {}
    visit_counts[start] = 1

    for line in lines:

        x = 0 
        y = 0

        for char in line:
            #print(char)
            match char: 

                case '>':
                    x += 1
                case '<':
                    x -= 1
                case '^':
                    y += 1
                case 'v':
                    y -= 1

                case _:
                    print("Error, did not recognize instruction")   

            #print("current coords", (x, y))     
            current_coord = (x, y)   
            if current_coord not in visit_counts:
                visit_counts[current_coord] = 1
            else:
                visit_counts[current_coord] += 1

    #print(visit_counts)
    sum = 0
    for value in visit_counts.values():
        if value >= 1:
            sum += 1
    return sum

def day03_part1_solution(lines: str) -> int:

    #print(lines)
    return solve(lines)