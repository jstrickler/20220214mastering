#!/usr/bin/env python

"""Basic sorting example"""

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

sorted_fruit = sorted(fruits)  # <1>

print(sorted_fruit)

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

sorted_nums = sorted(nums)
print(sorted_nums)

# INVALID:
# stuff = ['wombat', 'otter', 25, 37, 'mudhen']
# print(sorted(stuff))

x = [('m', 19), ('r', 3), ('m', 5), ('e', 17)]
print(sorted(x))

