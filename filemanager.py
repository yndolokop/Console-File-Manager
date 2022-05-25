import shutil
import os
import sys


def create_file_folder(file_name, folder_name):
    if not os.path.exists(file_name):
        open(file_name, "w")
    os.mkdir(folder_name)


def delete_file_folder(file_name, folder_name):
    os.remove(file_name)
    os.rmdir(folder_name)


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
