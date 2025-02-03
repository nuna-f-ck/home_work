from typing import Union


"""Функция принимает номер карты и маскирует его"""
def get_mask_card_number(num_card: Union[int]) -> int:
    num_card = str(num_card)
    block_1 = num_card[0:4]
    block_2 = num_card[4:6] + "**"
    block_3 = "****"
    block_4 = num_card[12:16]
    masck = block_1 + " " + block_2 + " " + block_3 + " " + block_4
    return masck


"""Функция принимает номер карты и возвращает его последние 4 цифры"""
def get_mask_account(num_card: Union[int]) -> int:
    num_card = str(num_card)
    masck = "**" + num_card[12:]
    return masck
