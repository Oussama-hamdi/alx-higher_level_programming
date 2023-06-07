#!/usr/bin/python3

def remove_char_at(str, index):
    if index < 0 or index >= len(str):
        return str
    return str[0: index] + str[index + 1:]
