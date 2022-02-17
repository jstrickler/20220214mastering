from math import pi

def get_message():
    return "Hello, Python world"

message = get_message()
print(message)

def double(a):
    return a * 2

print(double(5))
print(double(8.7))
print(double("huh?"))
print(double(['x', 'y', 'z']))

def circle_area(diameter):
    radius = diameter / 2
    return pi * (radius ** 2)

def rectangle_area(length, width):
    return length * width

def square_area(length):
    return rectangle_area(length, length)

print(circle_area(22))
print(rectangle_area(8, 19))
print(square_area(55))

def spam():
    print("spam spam spam")

x = spam()
print(x)

for i in range(10):
    spam()


print("ham", "eggs", "toast")
r = print("does it have a return value?")
print(r)

name = input("What is your name? ")
print("name is", name)

input("Press ENTER to continue")

print("OK")

x = 100  # GLOBAL (to this file)

def ham():
    x = 50  # still LOCAL
    m = "mutton"  # LOCAL variable
    print("x is", x)
    g = globals()  # g is dict of global variables
    print("global x is", g['x'])

ham()
# print("m is", m)
print("in main: x is", x)
# can't get to m from here






