#!/usr/bin/python3
'''
File that read files and prints it with stdout
'''


def read_file(filename=""):
    '''
    function that reads a file and prints
    with stdout
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
