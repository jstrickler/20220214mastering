
actor = "Chris Hemsworth"

print(actor, type(actor))


s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the former BDFL of Python")
print('Guido is the former "BDFL" of Python')

print("""Guido's the former "BDFL" of Python""")

notice = """
This code is (c) 2022 John Strickler
All rights reserved
"""

insert = """
insert into 
customers (name, state) 
values ('Bob', 'MI')
"""

actor = "Chris Hemsworth"

print(type(actor), len(actor))  # builtin (global) functions

print(actor.upper())
a = actor.upper()
print(a, actor)

#  obj.method()

print(actor.upper(), actor.lower())
print(actor.count('h'))
print(actor.count('or'))
print(actor.lower().count('h'))

# print(actor.count('h').lower())  not valid
print(actor.startswith('Chris'), actor.startswith('Liam'))
print(actor.endswith('spam'))
print("wor" in actor)
print("row" in actor)

print(actor.find('Chris'), actor.find('wor'), actor.find('row'))

s1 = "        All my exes live in Texas        "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

s2 = "xxxxxxxxxxyyyyyyyyyAll my exes live in Texasyyyyyyyyyyx"
print("|" + s2.lstrip("xy") + "|")
print("|" + s2.rstrip("xy") + "|")
print("|" + s2.strip("xy") + "|")
print()


record_1 = "Bob Smith Memphis TN"
data = record_1.split()
print(data)

record_2 = "Bob|Smith|Memphis|TN"
data = record_2.split('|')
print(data)



























