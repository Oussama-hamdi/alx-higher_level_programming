#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10
str = f"Last digit of {number} is {last_num} and is"
if (last_num == 0):
    print(f"{str} 0")
elif (last_num < 6):
    print(f"{str} less than 6 and not 0")
else:
    print(f"{str} greater than 5")
