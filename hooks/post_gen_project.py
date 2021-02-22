import os
import shutil


ignore_data_folder = "{{ cookiecutter.ignore_data}}" == "yes"

ignore_text = '''
# Ignore the data directory
data/
'''

if ignore_data_folder:
    with open(".gitignore", 'a') as ignore_file:
        ignore_file.write(ignore_text)
