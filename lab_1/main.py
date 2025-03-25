import constants
import func_for_encrypt
import func_for_decrypt
import func_info_text
import func_for_file


def main():
    try:
        encrypted_text_1 = func_for_encrypt.text_encrypting(constants.SOURCE_TEXT_1, constants.MATRIX)
        func_for_file.write_in_file(encrypted_text_1, constants.PATH_TO_WRITE_ENCRYPT_TEXT_1)
        print(encrypted_text_1)

        decrypted_text_1 = func_for_decrypt.text_decrypting(encrypted_text_1, constants.MATRIX)
        func_for_file.write_in_file(decrypted_text_1, constants.PATH_TO_WRITE_DECRYPT_TEXT_1)
        print(decrypted_text_1)

        func_for_file.write_in_file(str(func_info_text.word_chance_in_text(constants.SOURCE_TEXT_2)), constants.PATH_TO_WRITE_DESC_WORD_CHANCE)

        decrypted_text2 = func_for_decrypt.decrypting_text_with_key(constants.SOURCE_TEXT_2, constants.DECRYPTION_KEY)
        func_for_file.write_in_file(decrypted_text2, constants.PATH_TO_WRITE_DECRYPT_TEXT_2)
        print(decrypted_text2)
    except ValueError as error:
        print(f"{error}")

if __name__ == "__main__":
    main()


