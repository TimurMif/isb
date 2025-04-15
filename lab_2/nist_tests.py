import math
import re

from scipy.special import gammaincc

import constants


def frequency_test(sequence: str) -> float:
    """
    Implementing a frequency bitwise test from the NIST test suite
    :param sequence: The sequence that we are checking
    :return: The probability that determines the degree of randomness
    of the sequence
    """
    if not sequence:
        raise ValueError("Sequence is empty")
    sequence = re.sub("^\s+|\n|\r|\s+$", '', sequence)
    summ = 0
    for elem in sequence:
        if elem == '1':
            summ += 1
        elif elem == '0':
            summ -= 1
    sqrt_len = math.sqrt(len(sequence))
    s_n = summ/sqrt_len
    p_value = math.erfc(s_n/math.sqrt(2))
    return p_value

def identical_bits_test(sequence: str) -> float:
    """
    Implementing a test for identical consecutive bits
    :param sequence: The sequence that we are checking
    :return: The probability that determines the degree of randomness
    of the sequence
    """
    if not sequence:
        raise ValueError("Sequence is empty")
    sequence = re.sub("^\s+|\n|\r|\s+$", '', sequence)
    length = len(sequence)
    summ = 0
    for elem in sequence:
        if elem == "1":
            summ += 1
    zeta = summ/length
    if abs(zeta - 0.5) < 1/math.sqrt(length):
        v_n = 0
        for index in range(0, length - 1):
            if sequence[index] == sequence[index + 1]:
                v_n += 0
            else:
                v_n += 1
        p_value = math.erfc(abs(v_n - 2 * length * zeta * (1 - zeta)) /
                            (2 * math.sqrt(2 * length) * zeta * (1 - zeta)))
        return p_value
    else:
        return 0.0

def long_sequence_test(sequence: str) -> float:
    """
    Implementing a test for the longest sequence of units in a block
    :param sequence: The sequence that we are checking
    :return: The probability that determines the degree of randomness
    of the sequence
    """
    if not sequence:
        raise ValueError("Sequence is empty")
    sequence = re.sub("^\s+|\n|\r|\s+$", '', sequence)
    length = len(sequence)
    if length != 128:
        raise ValueError("The sequence must be 128 bits long.")
    array_sets = []
    categories_v = [0, 0, 0, 0]
    for index in range(0, length, 8):
        set = []
        for cur in range(0, 8):
            if sequence[index + cur] == "0" or sequence[index + cur] == "1":
                set.append(int(sequence[index + cur]))
            else:
                raise ValueError("The sequence should contain only 1 or 0")
        count_units = find_max_num_of_elem(set, 1)
        if count_units <= 1:
            categories_v[0] += 1
        elif count_units == 2:
            categories_v[1] += 1
        elif count_units == 3:
            categories_v[2] += 1
        elif count_units >= 4:
            categories_v[3] += 1
        array_sets.append(set)
    xi2 = 0
    for i in range(0, 4):
        xi2 += (((categories_v[i] - 16 * constants.ARRAY_PI[i])**2) /
                (16 * constants.ARRAY_PI[i]))
    p_value = gammaincc(1.5 , xi2 / 2)
    return p_value

def find_max_num_of_elem(array: list, elem: int) -> int:
    """
    A function for finding the maximum number of consecutive elements
    :param array: The array in which we are looking for
    :param elem: The element with which we are looking for a sequence
    :return: Maximum sequence of elements in an array
    """
    if not array:
        raise ValueError("Array is empty")
    if not elem:
        raise ValueError("Element is empty")
    max_count = 0
    count = 0
    for index in range(0, len(array)):
        if array[index] == elem:
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    return max_count