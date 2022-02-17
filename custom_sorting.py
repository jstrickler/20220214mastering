
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=str.lower)
print("f2: {}\n".format(f2))

f3 = sorted(fruits, key=len)
print("f3: {}\n".format(f3))

def ilen(x):
    return len(x), x.lower()   #  (4, 'kiwi')

f4 = sorted(fruits, key=ilen)
print("f4: {}\n".format(f4))

def ignore_case(fruit):
    return fruit.lower()

f5 = sorted(fruits, key=ignore_case)
print("f5: {}\n".format(f5))

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

for person in sorted(people):
    print(person)
print('-' * 60)



def by_dob(data):
    return data[1], data[0]   # data[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports.items())
for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)

def by_name(item):
    return item[1]

for code, name in sorted(airports.items(), key=by_name):
    print(code, name)
print('-' * 60)







