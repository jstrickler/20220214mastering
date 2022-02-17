import os

# for TUPLE in os.walk(START_DIR):
#
# TUPLE is dir_path, subdir_list, file_list

start_folder = "."

for dir_path, subdirs, files in os.walk(start_folder):
    if '.git' in subdirs:
        subdirs.remove('.git')
    print(dir_path)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")

