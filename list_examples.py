list1 = list()  # empty list
# x = list(iterable)
list2 = ['a', 'b', 'c']
list3 = []  # empty list

cities = ['Cheyenne', 'Newark', 'Indianapolis', 'Toronto']

print(cities)
x = repr(cities)
print(x)
print(len(cities), cities[0])

cities.append('Durham')
print("cities: {}".format(cities))
cities.append('Roanoke')
cities.append('Boston')
print("cities: {}".format(cities))
cities.insert(0, 'Sacramento')
cities.insert(5, 'Seattle')
print("cities: {}".format(cities))
cities[2] = "Morristown"
print("cities: {}".format(cities))

more_cities = ['Atlanta', 'Tampa', 'Miami']

# LIST.extend(iterable)
cities.extend(more_cities)
print("cities: {}".format(cities))

even_more_cities = ['Chicago', 'Topeka', 'Baton Rouge']
cities.append(even_more_cities)
print("cities: {}".format(cities))
print("cities[12]: {}".format(cities[12]))
print("cities[12][1]: {}".format(cities[12][1]))

x = cities[12]
print("x: {}".format(x))
print("x[1]: {}".format(x[1]))

#  LIST.append(obj)     add obj to end
#  LIST.insert(pos, obj)  insert obj at pos
#  LIST.extend(iterable)  append each obj in iterable

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']
x.extend(y)
print("x: {}".format(x))
x.append(y)
print("x: {}".format(x))

# del OBJ

print("cities: {}".format(cities))
print(cities.index('Morristown'))
del cities[2]  # remove 3rd element
print("cities: {}".format(cities))

c = cities.pop()
print("c: {}".format(c))
print("cities: {}".format(cities))

c = cities.pop(4)
print("c: {}".format(c))
print("cities: {}".format(cities))

cities.remove('Roanoke')
print("cities: {}".format(cities))

#  del LIST[pos]
#  LIST.pop()
#  LIST.pop(pos)
#  LIST.remove(value)

cities.append(even_more_cities)
print("cities: {}".format(cities))
del cities[9][1]
print("cities: {}".format(cities))

print(cities[0], cities[4], cities[8])

del cities[-1]
print("cities: {}".format(cities))

print("cities[-1]: {}".format(cities[-1]))
print()
print("cities[0:3]: {}".format(cities[0:3]))
print("cities[2:6]: {}".format(cities[2:6]))


print("cities[5:]: {}".format(cities[5:]))


actor = "Chris Hemsworth"
print("actor[:5]: {}".format(actor[:5]))
print("actor[-5:]: {}".format(actor[-5:]))

print("cities: {}".format(cities), '\n')

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

words = ["Python", "is", "wack"]
for word in words:
    print(word)
print()

#  for VAR in ITERABLE:
#      ...

#  There are 10 kinds of people who understand binary

a = 0b1001
b = 0xDeadBeef
c = 0o336362


name = "Wolcott"
for wombat in name:
    print(wombat)
print()

# for char in STR
# for obj in LIST
# for obj in TUPLE
# for byte in BYTES

junk = ['Fred', 5, None, 2.7, 88, 'Wombat']



print("cities: {}".format(cities))


letters1 = ['a', 'b', 'c']
letters2 = ['d', 'e', 'f']
all_letters = letters1 + letters2
print("all_letters: {}".format(all_letters))


a = 'foo'
b = 'bar'
c  = a + b
print("c: {}".format(c))


print('-' * 60)
print('Python!' * 5)

flags = [False] * 10
print("flags: {}".format(flags))

print("'Cheyenne' in cities: {}".format('Cheyenne' in cities))
print("'Laramie' in cities: {}".format('Laramie' in cities))

s = "I like wombats!"
print("'wombat' in s: {}".format('wombat' in s))




































