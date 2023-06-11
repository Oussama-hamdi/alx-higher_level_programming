#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = len(row)
        for n in row:
            if length > 1:
                print("{:d}".format(n), end=' ')
            else:
                print("{:d}".format(n), end='')
            length -= 1
        print("")
