import shutil
import os
import sys
'''
Добавлен декорвтор add_separator()
Добавлен try/except в функцию create_file_folder(). 
Добавлен try/except в функцию delete_file_folder(). 
'''

def add_separators(f):
    def inner(*args, **kwargs):
        print('*' * 30)
        result = f(*args, **kwargs)
        print('*' * 30)
        return result
    return inner


def create_file_folder(folder_name, file_name):
    try:
        if not os.path.exists(file_name):
            open(file_name, "w")
    except FileNotFoundError:
        print()
    finally:
        os.mkdir(folder_name)
        open(file_name, "w")


def delete_file_folder(file_name, folder_name):
    try:
        os.rmdir(folder_name)
    except FileNotFoundError:
        print()
    else:
        os.remove(file_name)
        os.rmdir(folder_name)
    finally:
        os.remove(file_name)


def copy_file_folder(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def list_files():
    result = []
    for item in os.listdir(os.path.join(os.getcwd())):
        if os.path.isfile(item):
            result.append(item)
    return result


def list_directories():
    result = []
    for i in os.listdir(os.path.join(os.getcwd())):
        if os.path.isdir(i):
            result.append(i)
    return result


def files_and_dirs_to_file():
    lst_of_files = []
    lst_of_directories = []
    for item in os.listdir(os.path.join(os.getcwd())):
        if os.path.isfile(item):
            lst_of_files.append(item)
    for i in os.listdir(os.path.join(os.getcwd())):
        if os.path.isdir(i):
            lst_of_directories.append(i)
    dict_files_dirs = dict(files=lst_of_files, dirs=lst_of_directories)
    return dict_files_dirs


def author_info():
    return 'Python creator Guido van Rossum as language overlord'


def change_dir(new_dir):
    return os.chdir(os.path.join(os.getcwd(), new_dir))


def quit_program():
    sys.exit(0)
