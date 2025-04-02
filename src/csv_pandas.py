import csv
import pandas as pd


def read_csv(filepath):
    try:
        with open(filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)


def read_pd(filepath):
    try:
        df = pd.read_excel(filepath)
        return dict(df)
    except FileNotFoundError as f:
        print(f)
    except Exception as e:
        print(e)
