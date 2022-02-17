# from module import name
from pprint import pprint

FILE_NAME = 'DATA/knights.txt'

def main():
    kdata = read_data()
    pretty_print(kdata)
    print()
    print(get_field(kdata, 'Arthur', 0))
    print(get_field(kdata, 'Bedevere', 3))
    print()
    print_name_and_title(kdata)

# business logic
def read_data():
    knight_info = dict()

    with open(FILE_NAME) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')

            knight_info[name] = title, color, quest, comment

    return knight_info

# display logic
def pretty_print(wombat):  # data is a parameter (local variable)
    print(wombat)

# business logic
def get_field(data, knight_name, field_number):
    return data[knight_name][field_number]


# display logic
def print_name_and_title(info):
    for name, data in info.items():
        print(data[0], name)

main()

