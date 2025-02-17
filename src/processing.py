def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list:
    '''Функция возвращает список словарей, у которых state соответствует значению, которая принимает функция'''
    new_state = []
    for d in list_dict:
        if d.get("state") == state:
            new_state.append(d)
    return new_state


def sort_by_date(values: list[dict], order: bool = True) -> list[dict]:
    '''Возвращает отсортированный список'''
    filtered_date = sorted(values, key=lambda value: value['date'], reverse=order)
    return filtered_date
