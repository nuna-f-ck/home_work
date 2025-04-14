from typing import Any
import os
import logging

# === Новый блок: путь к файлу лога ===
current_dir = os.path.dirname(__file__)  # Путь к текущему файлу .py
log_dir = os.path.join(current_dir, '..', 'logs')  # Папка logs — на уровень выше, если нужно
os.makedirs(log_dir, exist_ok=True)  # Создаем папку, если её нет

log_path = os.path.join(log_dir, 'mascks.log')  # Полный путь до файла лога

# === Твой код с этим путем ===
logger = logging.getLogger('mascks')
file_handler = logging.FileHandler(log_path)
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
    # if num_card == str:
    #     logger.error("Ошибка: Неккоректный номер карты")
    #     return "Неккоректный номер карты"
    # else:
    #     if len(str(num_card)) != 16:
    #         logger.error("Ошибка: Неккоректный номер карты")
    #         return "Неккоректный номер карты"
    # num_card = str(num_card)
    masck = num_card[0:5] + "**" + num_card[-4:]
    logger.info("Успешное завершение программы")
    return masck
