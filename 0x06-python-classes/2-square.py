#!/usr/bin/python3
"""Square class."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """init instance
            Args:
                size: size
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
