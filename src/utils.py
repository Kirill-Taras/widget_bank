import json
from json import JSONDecodeError
from typing import Any


def get_json_file(file_json: Any) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    :param file_json: путь к файлу
    :return: список с операциями
    """
    try:
        with open(file_json, encoding="utf-8") as data:
            operations = json.load(data)
    except FileNotFoundError:
        operations = list()
    except JSONDecodeError:
        operations = list()
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
        return float(operation["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
