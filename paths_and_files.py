import os
from datetime import datetime

FOLDER = 'DATA'
FILENAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILENAME)

print("file_path: {}".format(file_path))

dirname = os.path.dirname(file_path)
basename = os.path.basename(file_path)
absname = os.path.abspath(file_path)

print("dirname: {}".format(dirname))
print("basename: {}".format(basename))
print("absname: {}".format(absname))

file_size = os.path.getsize(file_path)
print("file_size: {}".format(file_size))
file_raw_timestamp = os.path.getmtime(file_path)
print("file_raw_timestamp: {}".format(file_raw_timestamp))
file_timestamp = datetime.fromtimestamp(file_raw_timestamp)
print("file_timestamp: {}".format(file_timestamp))
print("is file?", os.path.isfile(file_path))
print("is dir?", os.path.isdir(file_path))
print("exists?", os.path.exists(file_path))
print("split:", os.path.split(file_path))
print("splitext:", os.path.splitext(file_path))
print('-' * 60)
for entry in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, entry)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"{file_size:8d} {entry}")
print('-' * 60)





