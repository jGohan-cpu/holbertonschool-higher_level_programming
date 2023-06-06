#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    # Exclude the script name itself from the arguments
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print("1:", arguments[0])
    else:
        print(num_arguments, "arguments:")
        for i, argument in enumerate(arguments, start=1):
            print(i, ":", argument)
