#!/usr/bin/python3
'''This module creates a rectangle.'''


class Rectangle:
    '''This class defines an empty Rectangle.'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Docstring init
        Args:
            width (int)
            height (int)
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """ getter and setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter and setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """ Return perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """return rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        w = '#' * self.width + '\n'
        return (w * self.height)[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
