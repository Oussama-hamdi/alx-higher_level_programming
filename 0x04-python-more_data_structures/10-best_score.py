#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    keys_list = list(a_dictionary.keys())
    name = keys_list
    num = a_dictionary[keys_list[0]]
    for key in keys_list:
        if a_dictionary[key] > num:
            num = a_dictionary[key]
            name = key
    return name


