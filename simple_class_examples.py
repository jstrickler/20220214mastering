

# instance = CLASS()
colors = list()
flowers = list()
birds = list()

names = []   #  names = list()

with open('DATA/alice.txt') as alice_in:
    contents = alice_in.read()


print(type(alice_in))

if colors:
    print('foo')

for x in colors:
    print(x)


value = 56    #  value = int(56)
name = "Fred"   # name = str("Fred")

#  obj == instance

print(name.upper())  # str.upper(name)

#   OBJ.method()
#   CLASS.method(OBJ)    cf. 'self'

x = "Mary"
print(x.upper())  #  str.upper(x)

class Dog:   #   StudlyCaps   UpperCamelCase

    # constructor
    def __init__(self, name):
        self._pet_name = name   # instance attribute

    def bark(self, sound):
        print(f"{self._pet_name} says {sound}! {sound}!")

d1 = Dog("Nellie")  #  Dog.__init__(d1, "Nellie")
d2 = Dog("Andy")    #  Dog.__init__(d2, "Andy")

d1.bark("woof")   #  Dog.bark(d1, "woof")
d2.bark("yip")   #  Dog.bark(d2, "yip)

print(d1._pet_name)  # naughty programmer! no biscuit!!












