#!/usr/bin/python3
import sys

# Get the arguments passed to the program
arguments = sys.argv[1:]

# Initialize the variable to hold the sum
sum_of_arguments = 0

# Iterate over each argument and add it to the sum
for arg in arguments:
    sum_of_arguments += int(arg)

# Print the sum
print(sum_of_arguments)
