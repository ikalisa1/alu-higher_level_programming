#!/usr/bin/python3
""" Creates an empty class called Rectangle
"""


class Rectangle:
    """ Empty class using pass
    """
    number_of_instances = 0

    def _init_(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self._height * self._width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self._height + 2 * self._width

    def _str_(self):
        if self._height <= 0 or self._width <= 0:
            return ""
        string = ""
        for i in range(self.__height):
            string += "#" * self.__width
            string += '\n'
        return string

    def _repr_(self):
        if self._height <= 0 or self._width <= 0:
            return ""
        string = ""
        string = "Rectangle(" + str(self.width) + ", " + str(self.height)
        string += ")\n"
        return string

    def _del_(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
