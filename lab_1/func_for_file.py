import json

def read_from_file(path_to_file: str) -> str:
    """
    Reads the contents of the file
    :param path_to_file: Path to file
    :return content: Content from file
    """
    content = ""
    with open(path_to_file, 'r') as file:
        content = file.read()
    return content

def write_in_file(content: str, path_to_file: str) -> str:
    """
    Writes content to a file
    :param path_to_file: Path to file
    :param content: Content to write
    :return content: Content
    """
    with open(path_to_file, 'w') as file:
        file.write(content)
    return content

def read_from_json_file(path_to_file: str):
    """
    Reads the contents of a json file
    :param path_to_file: Path to file
    :return : Content from file
    """
    with open(path_to_file, 'r', encoding='utf-8') as f:
        loaded_matrix = json.load(f)
    return loaded_matrix
