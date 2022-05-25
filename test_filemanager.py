
from filemanager import list_files, list_directories, files_and_dirs_to_file


def test_separator():
    count = 5
    assert '*' * count == '*****'


def test_list_files():
    assert list_files() != ['']
    assert list_files() != []


def test_list_directories():
    assert list_directories() == ['.git', '.idea', '.pytest_cache', 'venv', '__pycache__']


def test_files_and_dirs_to_file():
    r = files_and_dirs_to_file()
    if isinstance(r, list):
        assert 'main.py' in r
