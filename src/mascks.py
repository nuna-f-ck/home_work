from typing import Any


def get_mask_card_number(num_card: Any) -> Any:
    """Функция принимает номер карты и маскирует его"""
    if num_card == str:
        return "Неккоректный номер карты"
    if len(num_card) != 8:
        return "Неккоректный номер карты"
    num_card = str(num_card)
    block_1 = num_card[0:4]
    block_2 = num_card[4:6] + "**"
    block_3 = "****"
    block_4 = num_card[12:16]
    masck = block_1 + " " + block_2 + " " + block_3 + " " + block_4
    return masck


def get_mask_account(num_card: Any) -> Any:
    """Функция принимает номер карты и возвращает его последние 4 цифры"""
    if num_card == str:
        return "Неккоректный номер карты"
    if len(num_card) != 8:
        return "Неккоректный номер карты"
    num_card = str(num_card)
    masck = "**" + num_card[-4:]
    return masck
