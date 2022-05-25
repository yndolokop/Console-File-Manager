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
WRITE_CURRENT_DIR_TO_FILE = 'сохранить содержимое рабочей директории в файл'
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
    WRITE_CURRENT_DIR_TO_FILE,
    AUTHOR_INFO,
    CHANGE_CURRENT_DIR,
    MY_BANK_ACCOUNT,
    PLAY_VICTORINA,
    EXIT
)


def separator(count=30):
    return '*' * count


def create_file_or_directory():
    file_name = input('Введите имя файла: ')
    folder_name = input('Введите имя папки: ')
    filemanager.create_file_folder(file_name, folder_name)


def delete_file_or_directory():
    file_name = input('Введите имя файла: ')
    folder_name = input('Введите имя папки: ')
    filemanager.delete_file_folder(file_name, folder_name)


def copy_file_or_directory():
    name = input('Введите имя файла: ')
    new_name = input('Введите имя копиии: ')
    filemanager.copy_file_folder(name, new_name)


def print_files_in_project():
    files = filemanager.list_files()
    for item in files:
        print(item)


def print_directories_in_project():
    directories = filemanager.list_directories()
    for item in directories:
        print(item)

def write_files_and_dirs_to_json():
    dir_name = input('Введите имя директории: ')
    files_dir_list = filemanager.files_and_dirs_to_file()
    print(files_dir_list)
    with open(dir_name, 'w') as f:
        json.dump(files_dir_list, f)


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
    WRITE_CURRENT_DIR_TO_FILE: write_files_and_dirs_to_json,
    AUTHOR_INFO: print_author,
    CHANGE_CURRENT_DIR: print_change_dir,
    MY_BANK_ACCOUNT: run_my_bank_account,
    PLAY_VICTORINA: play_victorina,
    EXIT: filemanager.quit_program
}


def print_main_menu():
    print(separator())
    # Выводим названи пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}. {item}')
    print(separator())


def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and 0 < int(choice) <= len(menu_items)

# return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)

if __name__ == '__main__':
    # цикл основной программы
    while True:
        # рисуем меню
        print_main_menu()
        # пользователь выбирает цифру
        choice = input('Выберите пункт меню ')
        # проверяем что это корректный выбор
        if is_correct_choice(choice):
            # получаем назвнание пункта меню по номеру
            # choice - 1, т.к. в меню пункты выводятся с 1 а в картеже хранятся с 0
            choice_name = menu_items[int(choice) - 1]
            # получаем действие в зависимости от пунктам меню
            action = actions[choice_name]
            # вызываем функцию
            action()
        else:
            print('Неверный пункт меню')
