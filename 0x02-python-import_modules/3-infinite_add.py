#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0

    for num in range(len(argv) - 1):
        sum += int(argv[num + 1])
    print("{}".format(sum))
