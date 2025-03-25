def decrypting_code_num(row: str, column: str, key_matrix: list) -> str:
    """
    The function takes the coordinates of a symbol in the matrix from a string
    and returns the symbol.
    :param row: Index row
    :param column: Index column
    :param key_matrix: Matrix-key
    :return key_matrix[int(row)][int(column)]: Symbol from matrix
    """
    return key_matrix[int(row)][int(column)]

def text_decrypting(text: str, key_matrix: list) -> str:
    """
    A function that decrypts text. To do this, use a string from the indexes of
    the characters in the matrix and the matrix by which the text was encrypted.
    :param text: Encrypted text
    :param key_matrix: Matrix-key
    :return result_string: Decrypted text
    """
    result_string = ""
    for index in range(0, len(text), 2):
        result_string += (
            decrypting_code_num(text[index],
            text[index + 1], key_matrix)
        )
    return result_string

def decrypting_text_with_key(text: str, key: dict) -> str:
    """
    A function that decrypts text using the received dictionary key.
    :param text: Encrypted text
    :param key: Dictionary-key
    :return text: Decrypted text
    """
    for key, value in key.items():
        text = text.replace(key, value)
    return text
