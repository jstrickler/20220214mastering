i = 0
while i < 3:
    print("i is", i)
    i += 1
print()

while True:
    name = input("What is your name (or q to quit)? ")
    if name == 'q':
        break   # exit loop
    if name == '':
        continue  # go to top of loop
    print(f"{name} is in the club")

# name = ""
# while name != 'q':
#     name = input("What is your name? ")
#     if name != 'q':
#         print("Welcome,", name)
