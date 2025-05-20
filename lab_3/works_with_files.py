from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def write_file(path_to_file, content):
    """
    A function for bitwise writing of data to a file
    :param path_to_file: Path to file
    :param content: The data that we write to the file
    """
    print(f"Сохранение данных в файл {path_to_file}...")
    try:
        with open(path_to_file, 'wb') as f:
            f.write(content)
        print(f"||Данные успешно сохранены||")
    except Exception as e:
        print(f"Error: Произошла ошибка при сохранении в файл {e}")
        exit(1)


def read_file(path_to_file):
    """
    A function for bitwise reading of data from a file
    :param path_to_file: Path to file
    :return Content from file
    """
    print(f"Чтение данных из файла {path_to_file}...")
    try:
        with open(path_to_file, 'rb') as f:
            content = f.read()
        print(f"||Данные успешно прочитаны||")
        return content
    except FileNotFoundError:
        print(f"Error: Файл не найден")
        exit(1)
    except Exception as e:
        print(f"Error Произошла ошибка при чтении в файла {e}")
        exit(1)


def read_private_key(path_to_key):
    """
    Reading the private key from a file
    :param path_to_key: Path to private RSA key
    :return: Private key
    """
    print(f"Загрузка закрытого ключа из файла {path_to_key}...")
    try:
        with open(path_to_key, 'rb') as f:
            private_key = load_pem_private_key(f.read(), password=None)
        print("||Приватный ключ загружен!||")
        return private_key
    except FileNotFoundError:
        print(f"Error: Файл приватного ключа не найден по пути {path_to_key}")
        exit(1)
    except Exception as e:
        print(f"Error: Произошла ошибка при загрузки закрытого ключа {e}")
        exit(1)


def read_public_key(path_to_key):
    """
    Reading the public key from a file
    :param path_to_key: Path to public RSA key
    :return: Public key
    """
    print(f"Загрузка открытого ключа из файла {path_to_key}...")
    try:
        with open(path_to_key, 'rb') as f:
            public_key = load_pem_public_key(f.read())
        print("||Открытый ключ загружен||")
        return public_key
    except FileNotFoundError:
        print(f"Error: Файл открытого ключа не найден по пути {path_to_key}")
        exit(1)
    except Exception as e:
        print(f"Error: Произошла ошибка при загрузки открытого ключа {e}")
        exit(1)


def decrypt_symmetric_key(private_key, encrypted_symmetric_key):
    """
    A function for decrypting a symmetric key using a private RSA key
    :param private_key: Private key
    :param encrypted_symmetric_key: Encrypted symmetric key
    :return: Decrypted symmetric key
    """
    print("Расшифровка симметричного ключа в процессе...")
    try:
        decrypted_symmetric_key = private_key.decrypt(
            encrypted_symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("||Симметричный ключ успешно расшифрован!||")
        return decrypted_symmetric_key
    except Exception as e:
        print(f"Error: Произошла ошибка при расшифровке симметричного ключа {e}")
        exit(1)


