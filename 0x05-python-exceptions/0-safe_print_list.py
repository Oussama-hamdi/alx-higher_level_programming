#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    nd_printed = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_printed += 1

        except IndexError:
            continue

    print()
    return nb_printed
