#!/usr/bin/python3
"""This script displays a Rectangle class that with width & hight attributes"""


class Rectangle:
    """ Rectagle class with width & height"""
    def __init__(self, width=0, height=0):
        """init class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """define width"""
        return self.__width

    @width.setter
    def width(self, widthValue):
        """width value range"""
        if type(widthValue) != int:
            raise TypeError("width must be an integer")
        if widthValue < 0:
            raise ValueError("width must be >= 0")
        self.__width = widthValue

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, HeightValue):
        """ height value range"""
        if type(HeightValue) != int:
            raise TypeError("height must be an integer")
        if HeightValue < 0:
            raise ValueError("height must be >= 0")
        self.__height = HeightValue

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2
