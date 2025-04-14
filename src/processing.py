from datetime import datetime


def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list:
    '''Функция возвращает список словарей, у которых state соответствует значению, которая принимает функция'''
    new_state = []
    for d in list_dict:
        if d.get("state") == state:
            new_state.append(d)
    return new_state


def sort_by_date(values: list[dict], order: bool = True) -> list[dict]:
    '''Возвращает отсортированный список транзакций по дате'''
    try:
        sort_info = sorted(values, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%SZ'), reverse=order)
    except ValueError:
        sort_info = sorted(values, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=order)
    return sort_info
