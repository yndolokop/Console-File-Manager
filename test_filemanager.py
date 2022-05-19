import pyautogui
from my_bank_account import *
from victorina_famous_people import *
import os
import shutil


def test_console_file_manager():
    os.mkdir('folder_mk')
    assert 'folder_mk' in os.listdir()

    original = os.path.join(os.getcwd(), 'vvv.py')
    target = os.path.join(os.getcwd(), 'vv.py')
    shutil.copy(original, target)
    assert shutil.copyfile(original, target)

    os.rmdir('folder_mk')
    if os.path.exists("vv.py"):
        os.remove("vv.py")


def test_buy():                  # не знаю, можно так делать или нет, но тест проходит если из терминала набрать
    assert buy(0, 10) == 0       # 'pytest -s test_filemanager.py'
    pyautogui.keyDown("enter")
    assert buy(100, 10) > 0
    pyautogui.keyDown("enter")
    assert buy(100, 10) == 90
    assert '' in history_item
    assert 10 in history_price


def test_get_random_person():
    assert len(get_random_person()) == 2








