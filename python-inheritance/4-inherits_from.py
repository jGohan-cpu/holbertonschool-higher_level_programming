#!/usr/bin/python3
"""Module that checks if an object is an instance
of a class that inherited (directly or indirectly)
specified class."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
