def process_dimensions(dimensions: str) -> tuple[int, int, int]:


    """
    
    Helper function to take in string of dimensions and makes them 3 different ints 
    representing length, width, and height
    

    Parameters/Arguments:

    dimensions (str) dimesions of a box given as string in (l x w x h) format 
    
    Returns: 
    
    A tuple that contains the length, width, and height of a given box as ints

    
    """

    lxwxh = dimensions.split('x')
    #print(lxwxh)
    length = lxwxh[0]
    width = lxwxh[1]
    height = lxwxh[2]

    return (int(length), int(width), int(height))