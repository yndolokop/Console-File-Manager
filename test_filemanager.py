import os
from filemanager import list_files, list_directories, files_and_dirs_to_file


def test_separator():
    count = 5
    assert '*' * count == '*****'


# def test_create_file_folder():
#     os.mkdir('test_.py')
#     assert 'test_.py' in os.listdir()


# def test_files_and_dirs_to_file():


def test_list_files():
    assert list_files() != ['']
    assert list_files() != []


def test_list_directories():
    assert list_directories() == ['.git', '.idea', '.pytest_cache', 'venv', '__pycache__']


def test_files_and_dirs_to_file():
    assert if any([True for k,v in word_freq.items() if v == value])







# def test_console_file_manager():
#     os.mkdir('folder_mk')
#     assert 'folder_mk' in os.listdir()
#
#     original = os.path.join(os.getcwd(), 'vvv.py')
#     target = os.path.join(os.getcwd(), 'vv.py')
#     shutil.copy(original, target)
#     assert shutil.copyfile(original, target)
#
#     os.rmdir('folder_mk')
#     if os.path.exists("vv.py"):
#         os.remove("vv.py")
#
#
# def test_buy():  # не знаю, можно так делать или нет, но тест проходит если из терминала набрать
#     assert buy(0, 10) == 0  # 'pytest -s test_filemanager.py'
#     pyautogui.keyDown("enter")
#     assert buy(100, 10) > 0
#     pyautogui.keyDown("enter")
#     assert buy(100, 10) == 90
#     assert '' in history_item
#     assert 10 in history_price
#
#
# def test_get_random_person():
#     assert len(get_random_person()) == 2
