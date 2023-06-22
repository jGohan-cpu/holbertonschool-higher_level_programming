#!/usr/bin/python3
import json
'''
function takes a JSON
string and returns the
data structure
'''


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure.
    """
    return json.loads(my_str)
