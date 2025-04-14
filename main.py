from src.filters import open_json_csv_xlsx, filter_by_description, final_output
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date


def tist():
    while True:
        print('''Выберите необходимый пункт меню(1, 2 или 3):\n
        1. Получить информацию о транзакциях из JSON-файла\n
        2. Получить информацию о транзакциях из CSV-файла\n
        3. Получить информацию о транзакциях из XLSX-файла''')
        choice = input("Ваш выбор: ")
        if choice == '1':
            transactions = open_json_csv_xlsx("data/operations.json", 'json')
            break
        elif choice == '2':
            transactions = open_json_csv_xlsx("data/csv_file.csv", 'csv')
            break
        elif choice == '3':
            transactions = list(open_json_csv_xlsx("data/transaction_exel.xlsx", 'xlsx'))
            break
        else:
            print("Файл не найден, попробуйте еще раз.")
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию. "
                       "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ").strip().upper()
        if status not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f"Статус операции \"{status}\" недоступен.")
        else:
            transactions = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
            break
    if transactions:
        sort_date = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_date == 'да':
            sort_order = input("Отсортировать 1) по возрастанию или 2) по убыванию? ").strip().lower()
            if sort_order == '1':
                transactions = sort_by_date(transactions)
            elif sort_order == '2':
                transactions = sort_by_date(transactions, False)
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
        final_output(transactions)
    elif not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print("Не найдено ни одной транзакции с указанным статусом.")


tist()
