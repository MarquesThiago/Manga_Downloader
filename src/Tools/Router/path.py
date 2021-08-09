import os, sys

def abstract_path_now(file):
    full_path_file = os.path.abspath(file)
    return os.path.dirname(full_path_file)

def abstract_path(file , join):
    full_path_dir = abstract_path_now(file)
    return os.path.join(full_path_dir, join)