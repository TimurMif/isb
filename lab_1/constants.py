from func_for_file import read_from_file


PATH_TO_SOURCE_TEXT_1 = "source_text_task_1.txt"

PATH_TO_SOURCE_TEXT_2 = "source_text_task_2.txt"

PATH_TO_WRITE_ENCRYPT_TEXT_1 = "encrypted_text_1.txt"

PATH_TO_WRITE_DECRYPT_TEXT_1 = "decrypted_text_1.txt"

PATH_TO_WRITE_DECRYPT_TEXT_2 = "decrypted_text_2.txt"

PATH_TO_WRITE_DESC_WORD_CHANCE = "desc_word_chance.txt"

MATRIX = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
        ['Л', 'М', 'Н', 'О', 'П', 'Р'],
        ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
        ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
        ['Э', 'Ю', 'Я', '.', ',', ' ']
         ]

DECRYPTION_KEY = {
    'V' : ' ',
    'P' : 'о',
    'U' : 'э',
    '-' : 'т',
    'B' : 'п',
    'F' : 'д',
    'R' : 'и',
    'W' : 'р',
    'Z' : 'я',
    'M' : 'в',
    '9' : 'с',
    '$' : 'м',
    'J' : 'а',
    'Q' : 'щ',
    'O' : 'ф',
    'S' : 'ж',
    'E' : 'ы',
    'h' : 'б',
    'C' : 'й',
    'A' : 'х',
    'K' : 'л',
    '=' : 'ю',
    'I' : 'ш',
    'G' : 'ъ',
    '>' : 'ё',
    'x' : 'ь',
    'Y' : 'з',
    '3' : 'у',
    '8' : 'е',
    'L' : 'н',
    '!' : 'к',
    'n' : 'ц',
    't' : 'г',
    'd' : 'ч',
}

SOURCE_TEXT_1 = read_from_file(PATH_TO_SOURCE_TEXT_1)

SOURCE_TEXT_2 = read_from_file(PATH_TO_SOURCE_TEXT_2)
