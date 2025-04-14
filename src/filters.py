from src.mascks import get_mask_account
from src.utils import load_transactions
from src.csv_pandas import read_csv, read_pd
from src.widget import get_date
import re


def open_json_csv_xlsx(filepath, type=str):
    """
    Функция активирует другую необходимую функцию по запросу
    """
    if type == 'json':
        return load_transactions(filepath)
    if type == 'csv':
        return read_csv(filepath)
    if type == 'xlsx':
        return read_pd(filepath)


def filter_by_description(transactions, search_str):
    """
    Функция для фильтрации по описанию с использованием регулярных выражений
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx['description'])]


def final_output(transactions):
    try:
        for item in transactions:
            date = get_date(item['date'])
            description = item['description']
            to = get_mask_account(item['to'])
            amount = item['operationAmount']['amount'] + ' ' + item['operationAmount']['currency']['name']
            print(date + ' ' + description, to, 'Сумма: ' + amount, '', sep='\n')
    except KeyError:
        for item in transactions:
            date = get_date(item['date'])
            description = item['description']
            to = get_mask_account(item['to'])
            amount = str(item['amount']) + ' ' + item['currency_name'].lower()
            print(date + ' ' + description, to, 'Сумма: ' + amount, '', sep='\n')
            print(item['to'])

# a = [{'id': 176798279, 'state': 'CANCELED', 'date': '2019-04-18T11:22:18.800453',
#       'operationAmount': {'amount': '73778.48', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#       'description': 'Открытие вклада', 'to': 'Счет 90417871337969064865'},
#      {'id': 176798279, 'state': 'CANCELED', 'date': '2019-04-18T11:22:18.800453',
#       'operationAmount': {'amount': '73778.48', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#       'description': 'Открытие вклада', 'to': 'Счет 90417871337969064865'}]
#
# b = [{'id': '4377488', 'state': 'CANCELED', 'date': '2023-07-02T19:32:47Z', 'amount': '33265', 'currency_name': 'Ruble',
#       'currency_code': 'RUB', 'from': 'Discover 6505902114235361', 'to': 'Счет 35036089776755124501',
#       'description': 'Перевод организации'},
#      {'id': '4718690', 'state': 'CANCELED', 'date': '2021-10-22T18:06:24Z', 'amount': '24397', 'currency_name': 'Ruble',
#       'currency_code': 'RUB', 'from': 'Mastercard 8555423564337493', 'to': 'Счет 80979410926211688985',
#       'description': 'Перевод организации'}]
#
# c = [{'id': 3205257.0, 'state': 'PENDING', 'date': '2022-04-11T00:30:44Z', 'amount': 11280.0, 'currency_name': 'Ruble',
#       'currency_code': 'RUB', 'from': 'Mastercard 5612504218607911', 'to': 'Счет 96692813169753520384',
#       'description': 'Перевод организации'},
#      {'id': 3205257.0, 'state': 'PENDING', 'date': '2022-04-11T00:30:44Z', 'amount': 11280.0, 'currency_name': 'Ruble',
#       'currency_code': 'RUB', 'from': 'Mastercard 5612504218607911', 'to': 'Счет 96692813169753520384',
#       'description': 'Перевод организации'}]
