from sys import platform
import os
from random import randint

if platform == 'darwin':
    print('Mac')
elif platform == 'win32':
    print('Windows')
elif platform == 'linux' or platform == 'linux2':
    print('Linux')
else:
    print('Oopsie.')


def rename_files():
    file_path = r"/Users/kasperkristiansen/Desktop/secret_message"
    file_list = os.listdir(file_path)
    print(file_list)

    saved_path = os.getcwd()
    os.chdir(file_path)

    for file_name in file_list:
        new_file_name = str(randint(99, 9999)) + file_name + str(randint(99, 9999))
        print(file_name, '\tchanges to\t', new_file_name)
        os.rename(file_name, new_file_name)

    os.chdir(saved_path)


rename_files()
