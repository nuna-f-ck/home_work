from fileinput import filename
from functools import wraps


def open_write(file_name, function, ok_or_error=None):
    """Функция создана, чтобы упрощать работу функции log. Она открывает файл и записывает данные либо в консоль, либо в указанный файл"""
    if ok_or_error == "ok":
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'{function.__name__} ok')
        return function.__name__ + " ok"
    elif ok_or_error == "error":
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'{function.__name__}')
        return function.__name__ + " error"
    else:
        return function.__name__


def log(filename=None):
    """Функция логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if filename:
                    print(open_write(filename, func, "ok"))
                else:
                    print(f'{open_write(filename, func)}, result = {func(*args, **kwargs)}')
                return func(*args, **kwargs)
            except Exception as e:
                if filename:
                    print(open_write(filename, func, "error"))
                else:
                    print(f'{open_write(filename, func)}, type error: {e.__class__}, input: {args, kwargs}')
            return func(*args, **kwargs)

        return inner

    return wrapper

# filename="mylog.txt"
# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x//y
#
# my_function(4, 0)
