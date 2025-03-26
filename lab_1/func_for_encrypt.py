def encrypting_symbol(char: str, key_matrix: list) -> str:
    """
    The function searches the matrix for the indexes of the passed character and
    writes them to the resulting string.
    :param char: Symbol
    :param key_matrix: Matrix-key
    :return result_str: Result string
    """
    if not char:
        raise ValueError("Char to encrypt is empty")

    if not ('А' <= char <= 'я' or char in ' ,.!:;?""\n'):
        raise ValueError("Char is not on russian language")
    char_up_case = char.upper()
    result_str = ""
    for row in range(0, len(key_matrix)):
        for column in range(0, len(key_matrix[row])):
            if key_matrix[row][column] == char_up_case:
                result_str += str(row)
                result_str += str(column)
                return result_str
    return result_str

def text_encrypting(text: str, key_matrix: list) -> str:
    """
    The function encrypts the text by writing the line index and the index to the string
    the symbol column from the key matrix
    :param text: Text encrypt
    :param key_matrix: The key is the matrix with which we encrypt
    :return result_string: A string consisting of the indexes of each character in the matrix
    """
    if not text:
        raise ValueError("Text to encrypt is empty")
    if not all('А' <= char <= 'я' or char in ' ,.!:;?""\n' for char in text):
        raise ValueError("Text must consist of russian letters")
    result_string = ""
    for symbol in text:
        result_string += encrypting_symbol(symbol, key_matrix)
    return result_string
