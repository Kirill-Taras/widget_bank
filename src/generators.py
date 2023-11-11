from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    Функция, которая принимает список словарей,
    и возвращает итератор,
    который выдает по очереди операции, в которых указана заданная валюта.
    :param transactions: список операций.
    :param currency: валюта.
    :yield: операция по заданной валюте.
    """
    for operation in transactions:
        if operation['operationAmount']['currency']['code'] == currency:
            yield operation


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Функция, которая принимает список словарей
    и возвращает описание каждой операции по очереди.
    :param transactions: список операций.
    :yield: описание операции.
    """
    for operation in transactions:
        yield operation["description"]


def card_number_generator(first: int, last: int) -> Generator:
    """
    Функция, которая генерирует номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    :param first: От какой цифры начинается генерация.
    :param last: До какой цифры идет генерация.
    :yield: номер карты.
    """
    for operation in range(first, last + 1):
        number: str = "0" * (16 - len(str(operation))) + str(operation)
        number_card: str = " ".join([number[x: x + 4] for x in range(0, len(number), 4)])
        yield number_card
