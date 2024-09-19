def solve(lines: str) -> int:
    
    start = (0,0)
    visit_counts = {}
    visit_counts[start] = 2

    for line in lines:

        santa_x = 0 
        santa_y = 0
        robo_x = 0 
        robo_y = 0
        santa = True 

        for char in line:
            #print(char)
            match char: 

                case '>':
                    if santa:
                        santa_x += 1
                    else:
                        robo_x += 1 
                case '<':
                    if santa:
                        santa_x -= 1
                    else:
                        robo_x -= 1 
                case '^':
                    if santa:
                        santa_y += 1
                    else:
                        robo_y += 1 
                case 'v':
                    if santa:
                        santa_y -= 1
                    else:
                        robo_y -= 1 
                case _:
                    print("Error, did not recognize instruction")   

            #print("current coords", (x, y))     
            if santa:
                current_coord = (santa_x, santa_y)  
            if not santa:
                current_coord = (robo_x, robo_y)

            if current_coord not in visit_counts:
                visit_counts[current_coord] = 1
            else:
                visit_counts[current_coord] += 1

            #print(santa)
            santa = not santa 
            
            

    #print(visit_counts)
    sum = 0
    for value in visit_counts.values():
        if value >= 1:
            sum += 1
    return sum

def day03_part2_solution(lines: str) -> int:

    #print(lines)
    return solve(lines)