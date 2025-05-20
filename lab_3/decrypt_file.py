from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import os

import works_with_files

def symmetric_decrypt_chacha20(settings):
    """
    A function that decrypts data using the symmetric ChaCha20 algorithm and writes it to a file
    :param settings:  An object that stores parameters from a configuration file.
    """
    print("\n||Дешифрование информации||")
    path_to_initial = settings['encrypted_file']
    path_to_private_key = settings['secret_key']
    path_to_encrypted_sym_key = settings['encrypted_symmetric_key_file'] or settings['symmetric_key']
    path_to_decrypted_key = settings['decrypted_file']

    if not all([path_to_initial, path_to_private_key, path_to_encrypted_sym_key, path_to_decrypted_key]):
        print("Error: Не указаны все необходимые пути в настройках для дешифрования.")
        exit(1)
    if not os.path.exists(path_to_initial):
        print(f"Error: Зашифрованный файл не найден по пути {path_to_initial}")
        exit(1)
    if not os.path.exists(path_to_private_key):
        print(f"Error: Файл приватного ключа не найден по пути {path_to_private_key}")
        exit(1)
    if not os.path.exists(path_to_encrypted_sym_key):
        print(f"Error: Файл зашифрованного симметричного ключа не найден по пути {path_to_encrypted_sym_key}")
        exit(1)

    private_key = works_with_files.read_private_key(path_to_private_key)
    encrypted_sym_key_data = works_with_files.read_file(path_to_encrypted_sym_key)
    symmetric_key = works_with_files.decrypt_symmetric_key(private_key, encrypted_sym_key_data)

    print(f"Чтение зашифрованного файла {path_to_initial}...")
    encrypted_content = works_with_files.read_file(path_to_initial)
    nonce = works_with_files.read_file(settings['nonce'])

    print("Расшифровка в процессе...")
    plaintext = decrypt_chacha20(encrypted_content, symmetric_key, nonce)
    print("||Данные расшифрованы!||")

    print(f"Сохранение расшифрованных данных в {path_to_decrypted_key}...")
    works_with_files.write_file(path_to_decrypted_key, plaintext)
    print("||Дешифрование завершено успешно!||")

def decrypt_chacha20(encrypted_content, key, nonce):
    """
    A function that decrypts data using the symmetric ChaCha20 algorithm
    :param encrypted_content: Encrypted data
    :param key: The symmetric key that we will use to decrypt
    :param nonce: The random number used in the ChaCha20 algorithm
    :return: Decrypted data
    """
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(encrypted_content) + decryptor.finalize()
    return plaintext