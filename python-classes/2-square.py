#!/usr/bin/python3
"""class Square that must be  defined by (integer) size"""


class Square:
    """class with privte atribute"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
