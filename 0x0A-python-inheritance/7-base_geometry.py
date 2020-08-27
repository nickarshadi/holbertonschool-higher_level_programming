#!/usr/bin/python3
""" Module for Basegeometry class. """


class BaseGeometry:
    """ This is the BaseGeometry class."""

    def area(self):
        """ Get area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate integer. """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
