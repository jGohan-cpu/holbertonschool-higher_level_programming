#!/usr/bin/python3
"""
declaring class BaseGeometry
"""


class BaseGeometry:
    """
    defines area and integer
    """

    def area(self):
        """
        raises Exception prints error
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Args:
            name (_type_): name received
            value (_type_): value of name
        """
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f'{name} must be an integer')
        if value < 0:
            raise ValueError(f'{name} must be greater than 0')
