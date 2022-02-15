file_name = 'DATA/mary.txt'
#         open(path, mode)
mary_in = open(file_name, 'r')
for raw_line in mary_in:  # mary_in is a GENERATOR
    print(raw_line)
mary_in.close()
print('-' * 60)

# read line-by-line
with open(file_name) as mary_in:
    for raw_line in mary_in:  # raw_line has '\n' at end
        #  mary_in generator calls mary_in.readline()
        line = raw_line.rstrip() # strip '\n'
        print(line)
print('-' * 60)

# DON'T DO THIS:
# with open(file_name) as mary_in:
#     while True:
#         raw_line = mary_in.readline()
#         if len(raw_line) == 0:
#             break




# read entire file
with open(file_name) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents), '\n')
    print("normal:")
    print(contents)
print('-' * 60)

print("type(mary_in): {}\n".format(type(mary_in)))



# read into list of lines (with \n)
with open(file_name) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read into list of lines (without \n)
with open(file_name) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/breakfast.txt') as toothbrush:
    for line in toothbrush:
        print(line.rstrip())
print(toothbrush)

with open(file_name) as mary_in:
    with open('upper_mary.txt', 'w') as mary_out:
        for input_line in mary_in:
            output_line = input_line.upper()
            mary_out.write(output_line)


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitfile.txt', 'x') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


# file modes:
# 'r'  (or nothing)  read
# 'w' write
# 'a' append
# 'x' write if file does not exist



