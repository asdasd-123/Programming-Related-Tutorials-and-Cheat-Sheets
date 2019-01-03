"""
Example showing how to loop through a file tree
"""
import os

root_dir = r'C:\Programming'
file_set = set()

for dir_, _, files in os.walk(root_dir):
    for file_name in files:
        print('=====')
        rel_dir = os.path.relpath(dir_, root_dir)
        print(f'rel_dir : {rel_dir}')
        rel_file = os.path.join(rel_dir, file_name)
        print(f'rel_file : {rel_file}')
        file_set.add(rel_file)
