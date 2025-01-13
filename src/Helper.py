import re

def format_print(output):
    """
    Takes the output from a function call, formats it and stops the execution of the program
    :param output: {success : True/False, msg: "Error/Success message
    """
    
    RED = "\033[91m"
    GREEN = "\033[92m"

    if output["success"]:
        print(f"{GREEN}✓ {output["msg"]}")
    else:
        print(f"{RED}X {output["msg"]}")
        exit(1)


def valid_folder_name(folder_name: str) -> bool:
    """
    Ensure the string provided is a valid folder name
    :param folder_name: University name that will be used to create the folder
    """
    
    pattern = r'^(\w+\.?)*\w+$'
    return bool(re.match(pattern, folder_name))