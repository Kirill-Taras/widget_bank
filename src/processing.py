import re
from collections import Counter

from src.config import OPERATIONS_PATH
from src.utils import get_json_file

description = {
    "Перевод организации": 0,
    "Перевод со счета на счет": 0,
    "Открытие вклада": 0,
    "Перевод с карты на карту": 0,
}
operations_bank: list[dict] = get_json_file(OPERATIONS_PATH)


def get_data(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей
    и значение для ключа state, и возвращает новый список,
    содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение.
    :param data: список словарей с данными
    :param state: выполнено/отмененный
    :return: список словарей в зависимости от state
    """
    list_data: list = list()
    for data_state in data:
        if data_state["state"] == state:
            list_data.append(data_state)
    return list_data


def get_data_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты.
    :param data: список словарей с данными
    :param reverse: True/False (убывание/возрастание)
    :return: отсортированный список словарей с данными по дате
    """
    if reverse:
        return sorted(data, key=lambda x: x["date"], reverse=True)
    if not reverse:
        return sorted(data, key=lambda x: x["date"])


def get_data_by_str(operations: list, user_input: str) -> list[dict]:
    """
    Функция, которая принимет список словарей с данными о банковских операциях
    и строку поиска и возвращать список словарей, у которых в описании есть данная строка.
    :param operations: список словарей с данными о банковских операциях
    :param user_input: строка поиска
    :return: список словарей, у которых в описании есть данная строка поиска
    """
    result_list = list()
    for operation in operations:
        for key, value in operation.items():
            if key == "description" and (re.findall(pattern=user_input.lower(), string=value.lower(), flags=0)):
                result_list.append(operation)
    return result_list


def func_for_count(operations: list[dict], description_dict: dict) -> dict:
    """
    Функция, которая  принимает список словарей с данными о банковских операциях
    и словарь категорий операций и возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    :param operations: список словарей с данными о банковских операциях
    :param description_dict: словарь категорий операций
    :return: словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_description = list()
    for operation in operations:
        for key, value in operation.items():
            if operation[key] in list(description_dict.keys()):
                list_description.append(value)
    counted = dict(Counter(list_description))
    return counted
