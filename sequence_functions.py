nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print("nums: {}".format(nums))
print("fruits: {}".format(fruits))

print("len(nums), len(fruits): {} {}".format(len(nums), len(fruits)))

print("min(nums), min(fruits): {} {}".format(min(nums), min(fruits)))

print("sorted(nums): {}".format(sorted(nums)))
print("sorted(fruits): {}".format(sorted(fruits)))

print("sum(nums): {}".format(sum(nums)))

print("fruits: {}".format(fruits))
print("reversed(fruits): {}".format(reversed(fruits)))

rfruits = reversed(fruits)
for fruit in rfruits:
    # fruit = next(rfruits)
    # ...
    print(fruit)
print('-' * 60)

x = ['a', 'b', 'c']
for letter in x:
    print("letter: {}".format(letter))

y = [10, 20, 30, 40, 50]

m = zip(x, y)
print("m: {}".format(m))
for item in m:
    print(item)
print()

for letter, number in zip(x, y):
    print(letter, number)
print()

for fruit in fruits:
    print(fruit)
print('-' * 60)

for i, fruit in enumerate(fruits):
    print(i, fruit)
print('-' * 60)

print(list(enumerate(fruits)))

