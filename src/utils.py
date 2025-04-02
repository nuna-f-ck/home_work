# #C:\Users\Maslova.M\Downloads

import json

from black import JSONDecodeError

import logging

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def load_transactions(file_path):
    """
    Загружает данные из JSON-файла и возвращает список словарей.
    Если файл пустой или не найден, возвращает пустой список.
    """
    logger.info("Запуск программы")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Открытие файла")
                return data
            else:
                logger.error("Ошибка: данные в файле не являются списком.")
                print("Ошибка: данные в файле не являются списком.")
                return []
    except FileNotFoundError as f:
        logger.error("Файл не найден")
        print(f.__class__.__name__)
        return []
    except JSONDecodeError as j:
        logger.error("Файл пустой")
        print(j.__class__.__name__)
        return []


def amount_transactions(transaction):
    """
    функция принимает на вход транзакцию и возвращает сумму транзакции в рублях
    """
    logger.info("Запуск программы")
    code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    if code == 'RUB':
        logger.info("Вывод суммы транзакции")
        return f'Сумма транзакции: {float(amount)}'
    if code == 'USD' or code == 'EUR':
        try:
            import requests
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

            headers = {
                "apikey": "ASGSwsV9hDysr3nj501AtwrGtiPG8xLA"
            }

            response = requests.get(url, headers=headers)
            data = response.json()
            logger.info("Вывод суммы транзакции")
            print(data)
            return float(data["result"])
        except Exception as e:
            logger.error("Ошибка")
            print(e)
