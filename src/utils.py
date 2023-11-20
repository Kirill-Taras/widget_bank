import json
from json import JSONDecodeError

from src.config import LOG_UTILS
from src.logger import setup_logging


def get_json_file(file_json: str) -> list[dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    :param file_json: путь к файлу
    :return: список с операциями
    """
    try:
        with open(file_json, encoding="utf-8") as data:
            operations = json.load(data)
        log = setup_logging(__name__, LOG_UTILS)
        log.info("Файл прочитан")
    except (FileNotFoundError, JSONDecodeError):
        operations = list()
        log = setup_logging(__name__, LOG_UTILS)
        log.error("Ошибка при чтении файла")
    return operations


def get_operations(operation: dict) -> float | str:
    """
    Функция, которая принимает на вход одну транзакцию
    и возвращает сумму транзакции в рублях
    или ошибку ValueError,
    если транзакция была совершена в другой валюте.
    :param operation: транзакция
    :return: сумма транзакции/ошибка ValueError
    """
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        log = setup_logging(__name__, LOG_UTILS)
        log.info("Сумма транзакции получена в рублях")
        return float(operation["operationAmount"]["amount"])
    else:
        log = setup_logging(__name__, LOG_UTILS)
        log.error("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
