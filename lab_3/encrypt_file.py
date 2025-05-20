from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os

import works_with_files

def symmetric_encrypt_chacha20(settings):
    """
    A function that encrypts data using the symmetric ChaCha20 algorithm and writes it to a file
    :param settings:  An object that stores parameters from a configuration file.
    """
    print("\n||Шифрование информации с помощью алгоритма ChaCha20||")
    path_to_initial = settings['initial_file']
    path_to_private_key = settings['secret_key']
    path_to_encrypted_sym_key = settings['encrypted_symmetric_key_file']
    encrypted_file_path = settings['encrypted_file']
    if not path_to_encrypted_sym_key:
        path_to_encrypted_sym_key = settings['symmetric_key']


    if not all([path_to_initial, path_to_private_key, path_to_encrypted_sym_key, encrypted_file_path]):
        print("Error: Не указаны все необходимые пути в настройках для шифрования.")
        exit(1)
    if not os.path.exists(path_to_initial):
        print(f"Error: Исходный файл не найден по пути {path_to_initial}")
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

    print(f"Чтение файла {path_to_initial}...")
    content = works_with_files.read_file(path_to_initial)

    print("Шифрование в процессе...")
    nonce = os.urandom(16)
    ciphertext = encrypt_chacha20(content, symmetric_key, nonce)
    print("Процесс завершен")

    print(f"Сохранение зашифрованных данных в файл {encrypted_file_path}...")
    works_with_files.write_file(encrypted_file_path, ciphertext)
    print(f"Сохранение nonce в файл {settings['nonce']}...")
    works_with_files.write_file(settings['nonce'], nonce)

    print("||Шифрование и сохранение завершено успешно!||")

def encrypt_chacha20(content, key, nonce):
    """
    A function that encrypts data using the symmetric ChaCha20 algorithm
    :param content: Data that needs to be encrypted
    :param key: The symmetric key that we use to encrypt
    :param nonce: The random number used in the ChaCha20 algorithm
    :return Encrypted data
    """
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(content) + encryptor.finalize()
    return ciphertext