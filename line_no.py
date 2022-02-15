import sys

file_paths = sys.argv[1:]  # get file names from cmd line

for file_path in file_paths:
    with open(file_path) as file_in:
        for line_number, raw_line in enumerate(file_in, 1):
            print(line_number, raw_line.rstrip())

# for file_path in file_paths:
#     with open(file_path) as file_in:
#         line_number = 1
#         for raw_line in file_in:
#             print(line_number, raw_line.rstrip())
#             line_number += 1

