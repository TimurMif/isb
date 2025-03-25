def decrypting_code_num(row: str, column: str, key_matrix: list) -> str:
    """
    The function takes the coordinates of a symbol in the matrix from a string
    and returns the symbol.
    :param row: Index row
    :param column: Index column
    :param key_matrix: Matrix-key
    :return key_matrix[int(row)][int(column)]: Symbol from matrix
    """
    index_row = int(row)
    index_column = int(column)
    if index_row < 0 or index_row >= len(key_matrix):
        raise ValueError("Index row out of range")
    if index_column < 0 or index_column >= len(key_matrix[index_row]):
        raise ValueError("Index column out of range")
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
        try:
            appending_str = decrypting_code_num(text[index],
                            text[index + 1], key_matrix)
            result_string += appending_str
        except ValueError as error:
            print(f"{error}")
    return result_string

def decrypting_text_with_key(text: str, key: dict) -> str:
    """
    A function that decrypts text using the received dictionary key.
    :param text: Encrypted text
    :param key: Dictionary-key
    :return text: Decrypted text
    """
    if not text:
        raise ValueError("Text to encrypt is empty")
    if not key:
        raise ValueError("Key to decrypt is empty")
    for key, value in key.items():
        text = text.replace(key, value)
    return text
