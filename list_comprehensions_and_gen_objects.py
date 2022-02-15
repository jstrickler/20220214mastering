nums = [800, 80, 1000, 32, 255, 400, 5, 5000]


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    if f.startswith('p'):
        f0.append(f.upper())
print("f0: {}\n".format(f0))

# new_list = [expr for var in old_list]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

f2 = [len(f) for f in fruits]
print("f2: {}\n".format(f2))

f3 = [(f, len(f)) for f in fruits]
print("f3: {}\n".format(f3))

f4 = [f.upper() for f in fruits if f.startswith('p')]
print("f4: {}\n".format(f4))

f5 = [f.capitalize() for f in fruits]
print("f5: {}\n".format(f5))

# S.upper() S.lower() S.capitalize() S.title()

print("one two three".upper())
print("one two three".title())
print("one two three".capitalize())
print("123 one two three".capitalize())
print()

f6 = [f for f in fruits if f.startswith('p')]
print("f6: {}\n".format(f6))

print("nums: {}".format(nums))
f7 = [n * 10 for n in nums if n > 300]
print("f7: {}\n".format(f7))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print("dobs: {}\n".format(dobs))

# list comp: [expr for var in iterable]
# generator: (expr for var in iterable)
fruit_gen  = (f.upper() for f in fruits)  # SAVES MEMORY!!
print("fruit_gen: {}".format(fruit_gen))
for fruit in fruit_gen:
    print(fruit)
print()









