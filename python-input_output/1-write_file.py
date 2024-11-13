#!/usr/bin/python3
"""function that write a text file (UTF8) and return the number of lines written"""


def write_file(filename="", text=""):
    """write in text file (UTF8)"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
