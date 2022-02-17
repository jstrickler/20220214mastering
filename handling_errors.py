
file_name = 'DATA/wombats.txt'

try:
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except OSError as err:
    # print(type(err))
    # print(err)
    print("Sorry, unable to open", file_name)


with open('DATA/breakfast.txt') as breakfast_in:
    food =  breakfast_in.read().splitlines()
print()

print(food)
for index in 'spam', 3, 22, 0:
    try:
        print(index, end=' ')
        print(food[index])
    except (TypeError, IndexError) as err:
        print("**ERROR**", err)
print()

nums = [0, 800, 80, 0, 1000, 32, 255, 'abc', 400, 5, 5000]

for num in nums:
    try:
        result = 25 / num
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("WHOA!!!", err)
    else:
        print(result)

print()

print("ALL DONE")

