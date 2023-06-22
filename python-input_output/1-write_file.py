#!/usr/bin/python3
'''
function that writes a string 
to a text fiel returns 
the number of characters
'''


def write_file(filename="", text=""):
    '''
    Writes the given text string to a file and returns the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
        '''
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
