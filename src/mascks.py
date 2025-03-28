from typing import Any

import logging

logger = logging.getLogger('mascks')
file_handler = logging.FileHandler('logs/mascks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(num_card: Any) -> Any:
    """Функция принимает номер карты и маскирует его"""
    logger.info("Запуск программы")
    if num_card == str:
        logger.error("Ошибка: Неккоректный номер карты")
        return "Неккоректный номер карты"
    else:
        if len(str(num_card)) != 16:
            logger.error("Ошибка: Неккоректный номер карты")
            return "Неккоректный номер карты"
    num_card = str(num_card)
    block_1 = num_card[0:4]
    block_2 = num_card[4:6] + "**"
    block_3 = "****"
    block_4 = num_card[12:16]
    masck = block_1 + " " + block_2 + " " + block_3 + " " + block_4
    logger.info("Успешное завершение программы")
    return masck


def get_mask_account(num_card: Any) -> Any:
    """Функция принимает номер карты и возвращает его последние 4 цифры"""
    logger.info("Запуск программы")
    if num_card == str:
        logger.error("Ошибка: Неккоректный номер карты")
        return "Неккоректный номер карты"
    else:
        if len(str(num_card)) != 16:
            logger.error("Ошибка: Неккоректный номер карты")
            return "Неккоректный номер карты"
    num_card = str(num_card)
    masck = "**" + num_card[-4:]
    logger.info("Успешное завершение программы")
    return masck
