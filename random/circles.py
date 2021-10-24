from math import pi
import sys


def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative!")
    return pi*(r**2)


print(sys.path)
