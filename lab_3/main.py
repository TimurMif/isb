import argparse
import json
import os

import config
import decrypt_file
import encrypt_file
import keys_gen


def load_config_settings(path_to_file = None):
    """
    Function for loading parameters from a json file
    :param path_to_file: The path to the settings file
    :return: Configuration settings
    """
    print("Загрузка настроек...")
    settings = {
        "initial_file": config.initial_file,
        "encrypted_file": config.encrypted_file,
        "decrypted_file": config.decrypted_file,
        "encrypted_symmetric_key_file": getattr(config, 'encrypted_symmetric_key_file',
                                                config.symmetric_key),
        "public_key": config.public_key,
        "secret_key": config.secret_key
    }
    if path_to_file:
        print(f"Попытка загрузить настройки из JSON файла {path_to_file} ...")
        if not os.path.exists(path_to_file):
            print(f"Error: JSON файл настроек не найден по пути {path_to_file}")
        else:
            try:
                with open(path_to_file, 'r', encoding='utf-8') as file:
                    json_settings = json.load(file)
                settings.update(json_settings)
                print("||Настройки успешно обновлены из JSON файла||")
            except json.JSONDecodeError:
                print(f"Error: Неверный формат JSON файла {path_to_file}")
            except Exception as e:
                print(f"Error: Ошибка при загрузке настроек из файла {e}")

    print("||Настройки загружены!||")
    return settings

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation',
                       help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption',
                       help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption',
                       help='Запускает режим дешифрования')
    args = parser.parse_args()
    json_path = None
    if args.generation is not None:
        json_path = args.generation
    elif args.encryption is not None:
        json_path = args.encryption
    elif args.decryption is not None:
        json_path = args.decryption

    settings = load_config_settings(json_path if isinstance(json_path, str) else None)

    if args.generation is not None:
        keys_gen.generate_keys(settings)
    elif args.encryption is not None:
        encrypt_file.symmetric_encrypt_chacha20(settings)
    elif args.decryption is not None:
        decrypt_file.symmetric_decrypt_chacha20(settings)

if __name__ == "__main__":
    main()
