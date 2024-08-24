import os

base_dir = os.path.dirname(os.path.abspath(__file__))

absolute_paths = ["e:/", "f:/", "h:/", "d:/"]

# Convert absolute paths to relative paths
relative_paths = [os.path.relpath(abs_path, base_dir) for abs_path in absolute_paths]

print(relative_paths)