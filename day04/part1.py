import hashlib 


def get_md5_hash(input_string: str) -> str:


    """
    Computes the MD5 hash of a given string and returns it as a hexadecimal string.

    Parameters:
    input_string (str): The string to be hashed.

    Returns:
    str: The MD5 hash of the input string in hexadecimal format.
    """

    md5_hash = hashlib.md5(input_string.encode())
    #print(type(md5_hash.hexdigest()))
    return md5_hash.hexdigest()


def solve(lines: str) -> int:
    
    solution = False 

    for line in lines:
        #print(get_md5_hash(line))
        i = -1
        while not solution:

            i += 1
            output = get_md5_hash(line + str(i))
            if output[:5] == "00000":
                solution = True
            
            #print(output)
            

    return i     
            

def day04_part1_solution(lines: str) -> int:

    #print(lines)
    return solve(lines)