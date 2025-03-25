from constants import MATRIX, PATH_TO_WRITE_DECRYPT_TEXT_2
from constants import DECRYPTION_KEY
from constants import SOURCE_TEXT_1
from constants import SOURCE_TEXT_2
from constants import PATH_TO_WRITE_ENCRYPT_TEXT_1
from constants import PATH_TO_WRITE_DECRYPT_TEXT_1
from constants import PATH_TO_WRITE_DECRYPT_TEXT_2
from constants import PATH_TO_WRITE_DESC_WORD_CHANCE
from func_for_encrypt import text_encrypting
from func_for_decrypt import text_decrypting
from func_for_decrypt import decrypting_text_with_key
from func_info_text import word_chance_in_text
from func_for_file import write_in_file


def main():
    encrypted_text_1 = text_encrypting(SOURCE_TEXT_1, MATRIX)
    write_in_file(encrypted_text_1, PATH_TO_WRITE_ENCRYPT_TEXT_1)
    print(encrypted_text_1)

    decrypted_text_1 = text_decrypting(encrypted_text_1, MATRIX)
    write_in_file(decrypted_text_1, PATH_TO_WRITE_DECRYPT_TEXT_1)
    print(decrypted_text_1)

    write_in_file(str(word_chance_in_text(SOURCE_TEXT_2)), PATH_TO_WRITE_DESC_WORD_CHANCE)
    decrypted_text2 = decrypting_text_with_key(SOURCE_TEXT_2, DECRYPTION_KEY)
    write_in_file(decrypted_text2, PATH_TO_WRITE_DECRYPT_TEXT_2)
    print(decrypted_text2)

if __name__ == "__main__":
    main()


