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
    for i in transactions:
        if i['operationAmount']['currency']['code'] == currency:
            yield i


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Функция, которая принимает список словарей
    и возвращает описание каждой операции по очереди.
    :param transactions: список операций.
    :yield: описание операции.
    """
    for i in transactions:
        yield i["description"]


def card_number_generator(first_i: int, last_i: int) -> Generator:
    """
    Функция, которая генерирует номера карт
    в формате "XXXX XXXX XXXX XXXX", где X — цифра.
    :param first_i: От какой цифры начинается генерация.
    :param last_i: До какой цифры идет генерация.
    :yield: номер карты.
    """
    for i in range(first_i, last_i + 1):
        number: str = "0" * (16 - len(str(i))) + str(i)
        number_card: str = " ".join([number[x: x + 4] for x in range(0, len(number), 4)])
        yield number_card
