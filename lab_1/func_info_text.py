def word_chance_in_text(text: str) -> dict:
    """
    Calculates the probability of each character in the source text and returns
    the dictionary
    :param text: Source text
    :return sorted_result_dict: Dictionary
    """
    len_text = len(text)
    result_dict = {}
    for word in text:
        num_word_coincidence = text.count(word)
        word_chance = num_word_coincidence/len_text
        result_dict[word] = word_chance
    sorted_result_dict = dict(sorted(result_dict.items(),
                                     key=lambda item:
                                     item[1],
                                     reverse=True))
    return sorted_result_dict
