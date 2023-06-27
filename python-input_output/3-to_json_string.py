#!/usr/bin/python3
'''
receives an object file
returns the JSON representation
'''

import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.
    """
    return json.dumps(my_obj)
