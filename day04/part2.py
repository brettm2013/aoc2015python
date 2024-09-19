import hashlib 
import time 


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
    
    start_time = time.time()
    solution = False 

    for line in lines:
        #print(get_md5_hash(line))
        i = -1
        while not solution:

            i += 1
            output = get_md5_hash(line + str(i))
            if output[:6] == "000000":
                solution = True
            #print(output)

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} seconds")
    return i   

def day04_part2_solution(lines) -> int:

    #print(lines)

    return solve(lines)