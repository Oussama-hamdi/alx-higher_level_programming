#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

	if my_list == []: return 0

	for i, value in enumerate(my_list[0: x]):
		try:
			print("{:d}".format(value), end="")
		except IndexError:
			break
	print()
	return i + 1
