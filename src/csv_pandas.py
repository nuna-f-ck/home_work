import csv
import pandas as pd


def read_csv(filepath):
    """
    Функция открывает и выводит csv файл
    """
    try:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)


def read_pd(filepath):
    """
    Функция открывает и выводит xlsx файл
    """
    try:
        df = pd.read_excel(filepath)
        return df.to_dict(orient='records')
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)
