from src.filters import open_json_csv_xlsx, \
    filter_by_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date


def talk():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    while True:
        print('''Выберите необходимый пункт меню(1, 2 или 3):\n
        1. Получить информацию о транзакциях из JSON-файла\n
        2. Получить информацию о транзакциях из CSV-файла\n
        3. Получить информацию о транзакциях из XLSX-файла''')
        choice = input("Ваш выбор: ")
        if choice == '1':
            file_path = input("Введите путь к JSON-файлу: ")
            transactions = open_json_csv_xlsx(file_path, 'json')
            break
        else:
            print("Файл не найден, попробуйте еще раз.")
        if choice == '2':
            file_path = input("Введите путь к CSV-файлу: ")
            transactions = open_json_csv_xlsx(file_path, 'csv')
            break
        else:
            print("Файл не найден, попробуйте еще раз.")
        if choice == '3':
            file_path = input("Введите путь к XLSX-файлу: ")
            transactions = open_json_csv_xlsx(file_path, 'xlsx')
            break
        else:
            print("Файл не найден, попробуйте еще раз.")

    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. "
                       "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ").strip().lower()
        if status not in ['executed', 'canceled', 'pending']:
            print(f"Статус операции \"{status}\" недоступен.")
        else:
            transactions = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
            break
    if transactions:
        sort_date = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_date == 'да':
            sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            if sort_order == 'по возрастанию':
                transactions = sort_by_date(transactions)
            elif sort_order == 'по убыванию':
                transactions = sorted(transactions, False)
    show_only_rubles = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if show_only_rubles == 'да':
        transactions = filter_by_currency(transactions, 'RUB')

    filter_description = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if filter_description == 'да':
        search_str = input("Введите строку для поиска: ")
        transactions = filter_by_description(transactions, search_str)

    if transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for tx in transactions:
            print(f"{tx['date']} {tx['description']}")
            print(f"Сумма: {tx['amount']} {tx['currency']}")
            print()
    elif:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Не найдено ни одной транзакции с указанным статусом.")


talk()
