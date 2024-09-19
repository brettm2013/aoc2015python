from pathlib import Path



def read_lines_from_file(data_file_name: str) -> str:

    # below is good for linux 
    #file_path = Path(os.path.expanduser(file_path))

    # we look up 2 directories and go into data and 
    # data_file_name which is argument passed into our  
    file_path = Path(__file__).parent.parent/'data'/data_file_name

    #below gives me a string 
    #file_path = os.path.join(os.path.dirname(__file__), '..', 'data', data_file_name)
    #with open(file_path, 'r') as file:
    #    content = file.read_text().splitlines()
    

    return file_path.read_text().splitlines()
