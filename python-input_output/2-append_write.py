#!/usr/bin/python3
"""function that append text file (UTF8) and return the number of characters"""


def apoend_write(filename="", text=""):
    """add apoend in text file (UTF8)"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
