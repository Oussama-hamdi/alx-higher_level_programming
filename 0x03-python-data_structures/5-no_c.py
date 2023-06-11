#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for st in my_string:
        if st != 'c' and st != 'C':
            new_str += st
    return new_str
