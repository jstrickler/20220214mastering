import sys

print("sys.argv: {}".format(sys.argv))

for file_path in sys.argv[1:]:
    print("processing", file_path)


