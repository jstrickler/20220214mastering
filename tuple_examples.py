
p = ['Bill', 'Gates', 'Microsoft', '1955-10-24']
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(type(person), len(person), person[0])
print("person: {}".format(person))
print(person[0], person[1])

john_bd = 1956, 10, 31

bill_bd = person[-1]

date_parts = bill_bd.split('-')
print(date_parts[0])
year = int(date_parts[0])


print("person: {}".format(person))

# unpack
first_name, last_name, product, dob = person

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
print("people[0]: {}".format(people[0]))
print("people[0][1]: {}".format(people[0][1]))
print()

for person in people:
    print(person, person[0], person[1])
print('-' * 60)

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # first_name, last_name, product, dob = people[2]
    # ...
    print(first_name, last_name)
print('-' * 60)


