#!/usr/bin/python3
up = False
for i in reversed(range(97, 123)):
    if up is False:
        up = True
    else:
        i = i - 32
        up = False
    print("{:c}".format(i), end='')
