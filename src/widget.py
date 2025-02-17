from typing import Any

from src.mascks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card: str) -> Any:
    """Функция принимает либо номер счета, либо номер карты и маскирует его"""
    if "Счет" in account_or_card:
        return get_mask_account(account_or_card)
    else:
        return get_mask_card_number(account_or_card)


def get_date(time: Any) -> Any:
    """Функция принимает дату и возвращает ее в определенном формате"""
    time = time[0:10].split("-")
    time = ":".join(time[::-1])
    return time
