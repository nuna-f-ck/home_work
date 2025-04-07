from utils import load_transactions
from csv_pandas import import read_csv, read_pd
import re


def open_json_csv_xlsx(filepath, type=str)
    if type == 'json':
        return load_transactions(filepath)
    if type == 'csv':
        return read_csv(filepath)
    if type == 'xlsx':
        return read_pd(filepath)


# Функция для фильтрации по описанию с использованием регулярных выражений
def filter_by_description(transactions, search_str):
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx['description'])]

# Функция для подсчета количества операций по категориям
def count_operations_by_category(transactions, categories):
    category_count = {category: 0 for category in categories}
    for tx in transactions:
        for category in categories:
            if category.lower() in tx['description'].lower():
                category_count[category] += 1
    return category_count
