import sys

print("all of sys.argv:", sys.argv)
script_name = sys.argv[0]
file_name = sys.argv[1]

print(f"{script_name} is reading file {file_name}")

