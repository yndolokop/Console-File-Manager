import pyautogui
from my_bank_account import *
from victorina_famous_people import *
import os


def test_mkdir():
    os.mkdir('folder_mk')
    assert 'folder_mk' in os.listdir()

    os.rmdir('folder_mk')


# def test_buy():
#     assert buy(0, 10) == 0
#     pyautogui.keyDown("enter")
#     assert buy(100, 10) > 0
#     pyautogui.keyDown("enter")
#     assert buy(100, 10) == 90
#     assert '' in history_item
#     assert 10 in history_price


def test_get_random_person():

    assert len(get_random_person()) == 2








