#!/usr/bin/python3
"""function that append text file (UTF8) and return the number of characters"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.

        filename: The name of the file.
        text: The last string to append to the file.
    Returns:
        The number of characters that has been appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
