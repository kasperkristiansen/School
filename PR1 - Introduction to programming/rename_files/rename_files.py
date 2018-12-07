from sys import platform
import os

if platform == 'darwin':
    print('Mac')
elif platform == 'win32':
    print('Windows')
elif platform == 'linux' or platform == 'linux2':
    print('Linux')
else:
    print('Oopsie.')


def rename_files():
    file_path = r"/Users/kasperkristiansen/Desktop/"
    file_list = os.listdir(file_path)
    print(file_list)

    saved_path = os.getcwd()
    os.chdir(file_path)

    translate_table = str.maketrans('', '', '0123456789')
    for file_name in file_list:
        print(file_name, '\tchanges to\t', file_name.translate(translate_table))
        os.rename(file_name, file_name.translate(translate_table))

    os.chdir(saved_path)


rename_files()
