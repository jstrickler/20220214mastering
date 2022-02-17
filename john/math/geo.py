from math import pi  #  find math.py (which might be virtual)

ANIMAL = "wombat"

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return rectangle_area(length, length)
