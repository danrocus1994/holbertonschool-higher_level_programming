#!/usr/bin/python3
"""base geo module"""


class BaseGeometry:
    """base geo class"""
    def area(self):
        """area function raises area not implemeted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is an integer"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
