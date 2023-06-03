"""This is a project for CS 362 exploring continuous integration

Authors: Andrew Osborne, nextAuth, nextAuth
Date: Spring Quarter 2023
"""

import string


def is_str_valid(num_str):
    """Searches a string for invalid characters

    Returns:
    False if invalid characters are found, True if none are found
    """

    if isinstance(num_str, str) is not True:
        return False

    if len(num_str) == 0:
        return False

    if num_str.count('.') > 1:
        return False

    for c in num_str:
        if c not in (".", "-"):
            if string.hexdigits.find(c) == -1:
                return False

    return True


def conv_num(num_str):
    """Converts a string into a base 10 number

    Takes a string (num_str) and converts it into a base
    10 number (conv_number), and returns that number.

    Returns:
    conv_num as an int
    """

    if is_str_valid(num_str) is False:
        return None

    conv_number = 0
    negative_flag = False
    float_flag = False
    decimal_place = 0

    for i, c in enumerate(num_str):
        if i == 0:
            if c == "-":
                negative_flag = True
                continue
        if c == ".":
            float_flag = True
            decimal_place = i
            continue
        # get place value
        if float_flag is True:
            p_value = 10**(-(i - decimal_place))
        else:
            p_value = 10**(len(num_str) - (i+1))
        num_value = ord(c) - 48
        conv_number += p_value*num_value

    if negative_flag is True:
        conv_number = conv_number * -1
    return conv_number


def my_datetime(num_sec):
    """Docstring here

    Returns:
    """

    return None


def conv_endian(num, endian='big'):
    """Docstring here

    Returns:
    """

    return None
