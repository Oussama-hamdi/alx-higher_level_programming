#!/usr/bin/python3

def check_tuple(tup=()):
    if len(tup) < 2:
        if len(tup) == 1:
            tup = (tup[0], 0)
        else:
            tup = (0, 0)
    return tup


def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = check_tuple(tuple_a)
    tup2 = check_tuple(tuple_b)
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])
