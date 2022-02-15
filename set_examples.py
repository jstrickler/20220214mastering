brad_countries = ['Burkina Faso', 'Italy', 'Ghana',
                  'Japan', 'Denmark', 'Madagascar',
                  'Turkey', 'Turkey', 'Turkey',
                  'Bulgaria', 'Mexico', 'Canada', 'Estonia',
                  'Kazakhstan']
janet_countries = ['Italy', 'France', 'Japan', 'Estonia',
                   'Mexico', 'Turkey', 'Italy',
                   'Italy', 'Bulgaria', 'Ghana', 'Italy']

brad = set(brad_countries)
brad.add('Portugal')
janet = set(janet_countries)
janet.add('Denmark')
janet.add('Uruguay')

print("brad: {}".format(brad))
print("janet: {}".format(janet))

print("Common:", brad & janet)  # intersection
print("NOT Common:", brad ^ janet) # xor
print("All:", brad | janet)  # union
print("Janet only:", janet - brad)
print("Brad only:", brad - janet)
print()

with open('DATA/breakfast.txt') as breakfast_in:
    all_foods = breakfast_in.read().splitlines()
    unique_foods = set(all_foods)
print("unique_foods: {}".format(unique_foods))






