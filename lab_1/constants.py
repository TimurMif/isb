from func_for_file import read_from_file
from func_for_file import read_from_json_file


PATH_TO_SOURCE_TEXT_1 = "source_texts/source_text_task_1.txt"

PATH_TO_SOURCE_TEXT_2 = "source_texts/source_text_task_2.txt"

PATH_TO_WRITE_ENCRYPT_TEXT_1 = "encrypt_texts/encrypted_text_1.txt"

PATH_TO_WRITE_DECRYPT_TEXT_1 = "decrypt_texts/decrypted_text_1.txt"

PATH_TO_WRITE_DECRYPT_TEXT_2 = "decrypt_texts/decrypted_text_2.txt"

PATH_TO_WRITE_DESC_WORD_CHANCE = "desc_word_chance.txt"

PATH_TO_KEY_TEXT_1 = "keys/key_text_1.json"

PATH_TO_DECRYPT_TEXT_2 = "keys/decrypt_key_text_2.json"

MATRIX = read_from_json_file(PATH_TO_KEY_TEXT_1)

DECRYPTION_KEY = read_from_json_file(PATH_TO_DECRYPT_TEXT_2)

SOURCE_TEXT_1 = read_from_file(PATH_TO_SOURCE_TEXT_1)

SOURCE_TEXT_2 = read_from_file(PATH_TO_SOURCE_TEXT_2)
