MATRIX = [['А', 'Б', 'В', 'Г', 'Д', 'Е'],
          ['Ё', 'Ж', 'З', 'И', 'Й', 'К'],
          ['Л', 'М', 'Н', 'О', 'П', 'Р'],
          ['С', 'Т', 'У', 'Ф', 'Х', 'Ц'],
          ['Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь'],
          ['Э', 'Ю', 'Я', '.', ',', ' ']
          ]

file = open("source_text_task_2.txt", "r")
SOURCE_TEXT = file.read()
file.close()

ARRAY_LETTERS = {
    ' ': 0.128675,
    'о': 0.096456,
    'И': 0.075312,
    'Е': 0.072292,
    'А': 0.064841,
    'Н': 0.061820,
    'Т': 0.061619,
    'С': 0.051953,
    'Р': 0.040677,
    'В': 0.039267,
    'М': 0.029803,
    'Л': 0.029400,
    'Д': 0.026983,
    'Я': 0.026379,
    'К': 0.025977,
    'П': 0.024768,
    'З': 0.015908,
    'Ы': 0.015707,
    'Ь': 0.015103,
    'У': 0.013290,
    'Ч': 0.011679,
    'Ж': 0.010673,
    'Г': 0.009867,
    'Х': 0.008659,
    'Ф': 0.007249,
    'Й': 0.006847,
    'Ю': 0.006847,
    'Б': 0.006645,
    'Ц': 0.005034,
    'Ш': 0.004229,
    'Щ': 0.003625,
    'Э': 0.002416,
    'Ъ': 0.000000,
}


def coding_symbol(char: str) -> str:
    char_up_case = char.upper()
    result_str = ""
    for row in range(0, len(MATRIX)):
        for column in range(0, len(MATRIX[row])):
            if (MATRIX[row][column]
                    == char_up_case):
                result_str += str(row)
                result_str += str(column)
                return result_str
    return result_str


def decoding_num(row: int, column: int) -> str:
    return MATRIX[row][column]


def text_coding(text: str) -> str:
    result_string = ""
    for symbol in text:
        result_string += coding_symbol(symbol)
    return result_string


def text_decoding(text: str) -> str:
    result_string = ""
    for index in range(0, len(text), 2):
        result_string += (
            str(decoding_num(int(text[index]), int(text[index + 1]))))
    return result_string


def main():
    encrypted_text = text_coding("Привет, я пришел домой")
    print(encrypted_text)
    print(text_decoding(encrypted_text))


def word_chance_in_text(text: str) -> dict:
    len_text = len(text)
    result_dict = {}
    for word in text:
        num_word_coincidence = text.count(word)
        word_chance = num_word_coincidence / len_text
        result_dict[word] = word_chance
    sorted_result_dict = dict(sorted(result_dict.items(),
                                     key=lambda item:
                                     item[1],
                                     reverse=True))
    return sorted_result_dict


def decoding_text(text: str) -> str:
    dict_letters_chance = word_chance_in_text(text)
    for index in range(0, len(dict_letters_chance)):
        checked_index = index
        if (checked_index >= len(ARRAY_LETTERS)):
            checked_index = (len(ARRAY_LETTERS) - 1)
        text = text.replace(list(dict_letters_chance.keys())[index],
                            list(ARRAY_LETTERS.keys())[checked_index]
                            )
    return text


REPLACE_DICTIONARY = {
    'V': ' ',
    'P': 'о',
    'U': 'э',
    '-': 'т',
    'B': 'п',
    'F': 'д',
    'R': 'и',
    'W': 'р',
    'Z': 'я',
    'M': 'в',
    '9': 'с',
    '$': 'м',
    'J': 'а',
    'Q': 'щ',
    'O': 'ф',
    'S': 'ж',
    'E': 'ы',
    'h': 'б',
    'C': 'й',
    'A': 'х',
    'K': 'л',
    '=': 'ю',
    'I': 'ш',
    'G': 'ъ',
    '>': 'ё',
    'x': 'ь',
    'Y': 'з',
    '3': 'у',
    '8': 'е',
    'L': 'н',
    '!': 'к',
    'n': 'ц',
    't': 'г',
    'd': 'ч',
}


def decoding_text_with_key(text: str) -> str:
    for key, value in REPLACE_DICTIONARY.items():
        text = text.replace(key, value)
    return text
def new_d_t(text:str) -> str:
    dict_letters_chance = word_chance_in_text(text)
    text = text.replace(list(dict_letters_chance.keys())[0], list(ARRAY_LETTERS.keys())[0])
    text = text.replace(list(dict_letters_chance.keys())[1],list(ARRAY_LETTERS.keys())[1])
    text = text.replace('U', 'э')
    text = text.replace('-', 'т')
    text = text.replace('B', 'п')
    text = text.replace('F', 'д')
    text = text.replace('R', 'и')
    text = text.replace('W', 'р')
    text = text.replace('Z', 'я')
    text = text.replace('M', 'в')
    text = text.replace('9', 'с')
    text = text.replace('$', 'м')
    text = text.replace('J', 'а')
    text = text.replace('Q', 'щ')
    text = text.replace('O', 'ф')
    text = text.replace('S', 'ж')
    text = text.replace('E', 'ы')
    text = text.replace('h', 'б')
    text = text.replace('C', 'й')
    text = text.replace('A', 'х')
    text = text.replace('K', 'л')
    text = text.replace('=', 'ю')
    text = text.replace('I', 'ш')
    text = text.replace('G', 'ъ')
    text = text.replace('>', 'ё')
    text = text.replace('x', 'ь')
    text = text.replace('Y', 'з')
    text = text.replace('3', 'у')
    text = text.replace('8', 'е')
    #text = text.replace('н', 'р')
    text = text.replace('L', 'н')
    text = text.replace('!', 'к')
    text = text.replace('n', 'ц')
    text = text.replace('t', 'г')
    text = text.replace('d', 'ч')
    return text

if __name__ == "__main__":
    main()
    print(len(ARRAY_LETTERS))
    print(len(word_chance_in_text(SOURCE_TEXT)))

    print(word_chance_in_text(SOURCE_TEXT))
    print(SOURCE_TEXT)
    print(decoding_text(SOURCE_TEXT))

    print(decoding_text_with_key(SOURCE_TEXT))
