import json
import os.path
from json import JSONDecodeError
from pathlib import Path

import pandas as pd
from pandas import DataFrame

from src.config import LOG_UTILS
from src.logger import setup_logging


def get_json_file(file_json: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
    :param file_json: путь к файлу
    :return: список с операциями
    """
    try:
        with open(file_json, encoding="utf-8") as data:
            operations: list = json.load(data)
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


def get_file(file_path: Path) -> list | DataFrame:
    """
    Функция, которая принимает на вход путь к файлам: .csv, .json, .xlsx.
    И возвращает данные для чтения в python.
    :param file_path: путь к файлу
    :return: данные в формате python
    """
    file_name: str = os.path.basename(file_path)
    basename, extension = os.path.splitext(file_name)
    if extension == ".json":
        try:
            with open(file_path, encoding="utf-8") as data:
                operations: list | DataFrame = json.load(data)
            log = setup_logging(__name__, LOG_UTILS)
            log.info("Файл прочитан")
        except (FileNotFoundError, JSONDecodeError):
            operations = list()
            log = setup_logging(__name__, LOG_UTILS)
            log.error("Ошибка при чтении файла")
        return operations
    elif extension == ".csv":
        try:
            operations = pd.read_csv(file_path, encoding="utf-8", sep=";")
            log = setup_logging(__name__, LOG_UTILS)
            log.info("Файл прочитан")
        except (FileNotFoundError, UnicodeDecodeError):
            operations = list()
            log = setup_logging(__name__, LOG_UTILS)
            log.error("Ошибка при чтении файла")
        return operations
    elif extension == ".xlsx":
        try:
            operations = pd.read_excel(file_path)
            log = setup_logging(__name__, LOG_UTILS)
            log.info("Файл прочитан")
        except (FileNotFoundError, UnicodeDecodeError):
            operations = list()
            log = setup_logging(__name__, LOG_UTILS)
            log.error("Ошибка при чтении файла")
        return operations
    else:
        operations = list()
        log = setup_logging(__name__, LOG_UTILS)
        log.error("Неверный формат файла")
        return operations
