import sys
import re
import os

if len(sys.argv) < 3:
    print("Syntax: pyfind.py PATTERN file1 file2 ...")
    exit()

pattern = sys.argv[1]      # first arg is pattern
file_paths = sys.argv[2:]  # rest of args are files

# regex = re.compile(pattern)

for file_path in file_paths:
    with open(file_path) as file_in:
        file_name = os.path.basename(file_path)
        for raw_line in file_in:
            if re.search(pattern, raw_line):
                line = raw_line.rstrip()
                print(file_name, line)
