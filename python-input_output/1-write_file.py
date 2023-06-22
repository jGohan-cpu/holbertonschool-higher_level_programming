#!/usr/bin/python3
'''
function that returns the 
number of characters
'''


def write_file(filename="", text=""):
    '''

    '''
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
