"""
Example showing how to loop through a file tree
"""
import os

root_dir = r'C:\Programming'
file_set = set()

for dir_, _, files in os.walk(root_dir):
    for file_name in files:
        print('=====')
        full_dir = os.path.join(dir_, file_name)
        print(f'dir_ : {full_dir}')                 # Prints full path
        rel_dir = os.path.relpath(dir_, root_dir)
        print(f'rel_dir : {rel_dir}')   # Prints relative path (only folder)
        rel_file = os.path.join(rel_dir, file_name)
        print(f'rel_file : {rel_file}')  # Prints raltive path (with file name)
        file_set.add(rel_file)
