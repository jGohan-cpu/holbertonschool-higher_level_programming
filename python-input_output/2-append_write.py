#!/usr/bin/python3
'''
This module contains a function that
writes a string and returns
of characters
'''


def append_write(filename="", text=""):
    '''
    Appends the given text string to a file and returns the number of characters added.

    Args:
        filename (str): The name of the file to which the text will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
