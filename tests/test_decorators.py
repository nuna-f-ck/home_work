import pytest
from src.decorators import log, open_write, my_function, my_function_file


def test_log_file(capsys):
    @log(filename="mylog.txt")
    def my_function_log_file(x, y):
        return x + y

    my_function_log_file(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function_log_file ok\n"


def test_log(capsys):
    @log()
    def my_function_log(x, y):
        return x + y

    my_function_log(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function_log, result = 3\n"


def test_retry_decorator():
    with pytest.raises(Exception, match="Something went wrong!"):
        my_function()


def test_retry_decorator_file():
    with pytest.raises(Exception, match="Something went wrong!"):
        my_function_file()
