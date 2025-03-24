# #C:\Users\Maslova.M\Downloads

import json

from src.generators import transactions

from black import JSONDecodeError


def load_transactions(file_path):
    """
    Загружает данные из JSON-файла и возвращает список словарей.
    Если файл пустой или не найден, возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Ошибка: данные в файле не являются списком.")
                return []
    except FileNotFoundError as f:
        print(f.__class__.__name__)
        return []
    except JSONDecodeError as j:
        print(j.__class__.__name__)
        return []


def amount_transactions(transaction):
    code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    if code == 'RUB':
        return f'Сумма транзакции: {float(amount)}'
    if code == 'USD' or code == 'EUR':
        try:
            import requests
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": "ASGSwsV9hDysr3nj501AtwrGtiPG8xLA"
            }

            response = requests.get(url, headers=headers)

            status_code = response.status_code
            result = response.text
            print(result)
        except Exception as e:
            print(e)
