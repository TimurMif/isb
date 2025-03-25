def read_from_file(path_to_file: str) -> str:
    """
    Reads the contents of the file
    :param path_to_file: Path to file
    :return content: Content from file
    """
    content = ""
    file = open(path_to_file, "r")
    content = file.read()
    file.close()
    return content

def write_in_file(content: str, path_to_file: str) -> str:
    """
    Writes content to a file
    :param path_to_file: Path to file
    :param content: Content to write
    :return content: Content
    """
    file = open(path_to_file, "w")
    file.write(content)
    file.close()
    return content
