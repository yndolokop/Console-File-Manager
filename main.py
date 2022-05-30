"""
a) Добовлен тернальный оператор в блоке if __name__ == '__main__' для функции print_main_menu() line 149
б) Добовлен также декоратор для функции print_main_menu() line 115
г) Добавлен try/except в функцию create_file_or_directory(). Функция создает файл и папку без ошибок, если ввести имена
   и файла и папки. Создает также файл или папку по отдельности, если вводить имя или файла или только папки. До записи с
   помощью try/except была красная ошибка. Понятно, что можно разделить функцию на две и не будет никаких ошибок.
"""

import os
import json

from my_bank_account import run_my_bank_account
import filemanager
from victorina_famous_people import play_victorina


# Названия пунктов меню
CREATE_FILE_FOLDER = ' создать файл/папку'
DELETE_FILE_FOLDER = ' удалить (файл/папку)'
COPY_FILE_FOLDER = ' копировать (файл/папку)'
LIST_ONLY_FILES = ' посмотреть только файлы'
LIST_ONLY_FOLDERS = ' посмотреть только папки'
SAVE_DIR_CONTENT_TO_FILE = 'сохранить содержимое рабочей директории в файл'
AUTHOR_INFO = ' создатель программы'
CHANGE_CURRENT_DIR = ' смена рабочей директории'
MY_BANK_ACCOUNT = ' мой банковский счет'
PLAY_VICTORINA = ' играть в викторину'
EXIT = 'выход'

# Набор пунктов меню
menu_items = (
    CREATE_FILE_FOLDER,
    DELETE_FILE_FOLDER,
    COPY_FILE_FOLDER,
    LIST_ONLY_FILES,
    LIST_ONLY_FOLDERS,
    SAVE_DIR_CONTENT_TO_FILE,
    AUTHOR_INFO,
    CHANGE_CURRENT_DIR,
    MY_BANK_ACCOUNT,
    PLAY_VICTORINA,
    EXIT
)


def create_file_or_directory():
    file_name = input('Введите имя файла: ')
    folder_name = input('Введите имя папки: ')
    try:
        filemanager.create_file_folder(folder_name, file_name)
    except Exception as e:
        print(e)


def delete_file_or_directory():
    file_name = input('Введите имя файла: ')
    folder_name = input('Введите имя папки: ')
    try:
        filemanager.delete_file_folder(file_name, folder_name)
    except Exception as e:
        print(e)


def copy_file_or_directory():
    name = input('Создать копию файла/папки. Введите имя: ')
    new_name = input('Введите имя копиии: ')
    filemanager.copy_file_folder(name, new_name)


# original = input('file name ')
# target = input('file name ')
# original = os.path.join(os.getcwd(), f'{original}')
# target = os.path.join(os.getcwd(), f'{target}')
# shutil.copy(original, target)
def print_files_in_project():
    files = filemanager.list_files()
    for item in files:
        print(item)


def print_directories_in_project():
    directories = filemanager.list_directories()
    for item in directories:
        print(item)


def save_filenames_and_folders_to_json():
    dir_name = input('Введите имя директории: ')
    files_dirs = filemanager.files_and_dirs_to_file()
    for k, v in files_dirs.items():
        print(k, '-->', v)
    with open(dir_name, 'w') as f:
        json.dump(files_dirs, f)


def print_author():
    author = filemanager.author_info()
    print(author)


def print_change_dir():
    name_dir = input('Введите имя директории: ')
    filemanager.change_dir(name_dir)
    print(os.getcwd())


# Словарь действия связывает название пункта меню с той функцией которую нужно выполнить
actions = {
    CREATE_FILE_FOLDER: create_file_or_directory,
    DELETE_FILE_FOLDER: delete_file_or_directory,
    COPY_FILE_FOLDER: copy_file_or_directory,
    LIST_ONLY_FILES: print_files_in_project,
    LIST_ONLY_FOLDERS: print_directories_in_project,
    SAVE_DIR_CONTENT_TO_FILE: save_filenames_and_folders_to_json,
    AUTHOR_INFO: print_author,
    CHANGE_CURRENT_DIR: print_change_dir,
    MY_BANK_ACCOUNT: run_my_bank_account,
    PLAY_VICTORINA: play_victorina,
    EXIT: filemanager.quit_program
}


@filemanager.add_separators
def print_main_menu():
    # print(separator())
    # Выводим названи пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}. {item}')
    # print(separator())


def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and 0 < int(choice) <= len(menu_items)


if __name__ == '__main__':
    while True:
        print_main_menu()
        choice = input('Выберите пункт меню: ')
        '********************************************'
        '''
        action = actions[menu_items[int(choice) - 1]] if is_correct_choice(choice) else 'Неверный пункт меню'
        action()        
        Неудачная попытка записи тернальным оператором нижележащего кода. Так и не разобрался почему при вводе 
        или 0 или 12, или букв вместо цифр,- не переходит к условию ELSE, но выдает ошибку 'str object is not callable'.
        Хотя, при вводе пунктов, которые соответствуют меню, работает корректно.
        '''
        '*********************************************'
        if is_correct_choice(choice):
            choice_name = menu_items[int(choice) - 1]
            action = actions[choice_name]
            action()
        else:
            print('Неверный пункт меню. Введите номер пункта меню')


