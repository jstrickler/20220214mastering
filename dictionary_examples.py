
d1 = dict()
d2 = {'spam': 12, 'ham': 4, 'eggs': 99}
d3 = {}

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

print(len(airports), type(airports))

airports['IND'] = 'Indianapolis'
airports['DEN'] = 'Denver'

print("airports: {}".format(airports))

# LIST[pos]
# DICT[key]

print("airports['YYZ']: {}".format(airports['YYZ']))

# error!
# print("airports['CYS']: {}".format(airports['CYS']))

print("airports.get('CYS'): {}".format(airports.get('CYS')))
print("airports.get('RDU'): {}".format(airports.get('RDU')))
print("airports.get('CYS', 'NOT FOUND'): {}".format(airports.get('CYS', 'NOT FOUND')))

for key in 'CYS', 'YYZ', 'OBX', 'CHI', 'LMN', 'RDU':
    print(key, key in airports)
print()

# for key, value in DICT.items():

for code, name in airports.items():
    print(code, name)
print('-' * 60)

for code, name in sorted(airports.items()):
    print(code, name)
print('-' * 60)


















