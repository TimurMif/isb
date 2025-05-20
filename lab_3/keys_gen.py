from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

import os

import works_with_files

def generate_symmetric_key():
    """
    A function that generates a symmetric encryption key
    :return: Generated symmetric encryption key
    """
    print("Генерация симметричного ключа ChaCha20 (256 бит)...")
    symmetric_key = os.urandom(32)
    print("||Симметричный ключ сгенерирован!||")
    return symmetric_key


def generate_rsa_keys(settings):
    """
    A function for generating an RSA key pair
    :param settings: An object that stores parameters from a configuration file.
    """
    print("Генерация пары RSA ключей (размер 2048 бит)...")
    try:
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()

        public_pem = settings['public_key']
        with open(public_pem, 'wb') as public_out:
            public_out.write(
                public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                        format=serialization.PublicFormat.SubjectPublicKeyInfo))

        print(f"Публичный ключ сохранен в {settings['public_key']}")
        private_pem = settings['secret_key']
        with open(private_pem, 'wb') as private_out:
            private_out.write(
                private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                          format=serialization.PrivateFormat.TraditionalOpenSSL,
                                          encryption_algorithm=serialization.NoEncryption()))
        print(f"Приватный ключ сохранен в {settings['secret_key']}")
        return private_key, public_key
    except Exception as e:
        print(f"Error: Произошла ошибка при генерации или сохранении ключей {e}")
        exit(1)


def encrypt_symmetric_key(public_key, symmetric_key, path_to_save):

    """
    A function for encrypting a symmetric key using an RSA public key
    :param public_key: RSA public key
    :param symmetric_key: The symmetric key that needs to be encrypted
    :param path_to_save: Path to save encrypted symmetric key
    """
    print(f"Шифрование симметричного ключа с помощью открытого ключа и сохранение в {path_to_save}...")
    try:
        encrypted_symmetric_key = public_key.encrypt(symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(
                    algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        works_with_files.write_file(path_to_save, encrypted_symmetric_key)
        print(f"Зашифрованный симметричный ключ сохранен в {path_to_save}.")
    except Exception as e:
        print(f"Error: Произошла ошибка при шифровании или сохранении ключа {e}")
        exit(1)


def generate_keys(settings):
    """
    A function that calls other key generation functions
    :param settings: An object that stores parameters from a configuration file.
    """
    print("\n||Генерация ключей||")
    symmetric_key = generate_symmetric_key()
    private_key, public_key = generate_rsa_keys(settings)
    encrypted_sym_key_path = settings.get('encrypted_symmetric_key_file')
    if not encrypted_sym_key_path:
        encrypted_sym_key_path = settings.get('symmetric_key')
        if not encrypted_sym_key_path:
            print("Error: Не указан путь для сохранения зашифрованного симметричного ключа в файле конфигурации.")
            exit(1)
    encrypt_symmetric_key(public_key, symmetric_key, encrypted_sym_key_path)
    print("||Генерация ключей завершена успешно!||")