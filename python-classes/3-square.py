#!/usr/bin/python3
"""class Square that must be  defined by (integer) size + area"""


class Square:
    """class with size attribute"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
