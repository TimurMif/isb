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

def write_report_in_file(path_to_file: str, label: str, c_score: float, j_score: float) -> str:
    """
    :param path_to_file: Path to file
    :param label: Label of report
    :param c_score: Score C++ consequence
    :param j_score: Score Java consequence
    :return: Label of report
    """
    with open(path_to_file, 'a') as file:
        file.write(label)
        c_str = "\nC++ sequence: " + str(c_score)
        file.write(c_str)
        j_str = "\nJava sequence: " + str(j_score)
        file.write(j_str)
    return label
