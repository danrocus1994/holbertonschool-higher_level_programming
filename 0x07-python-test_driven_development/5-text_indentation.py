#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Text_indentation function"""
    buffer = []
    l = len(text) - 1
    for i, char in enumerate(text):
        buffer.append(char)
        if char == ':' or char == '.' or char == '?':
            print("".join(buffer).strip())
            print()
            buffer = []
        elif i == l:
            print("".join(buffer).strip(), end="")
