#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = "{}".format(number)
last = int(last[-1])
if number < 0:
    last = last * (-1)
print("Last digit of {} is {} ".format(number, last), end='')
if last > 5:
    print("and is grater than 5")
elif last < 6 and last != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
