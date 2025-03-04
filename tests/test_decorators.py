import pytest
from src.decorators import log, open_write


def test_log_file(capsys):
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function, result = 3\n"
