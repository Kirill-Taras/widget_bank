from datetime import datetime

from src.masks import card_encryption, account_encryption


def card_type_number(user_input: str) -> str:
    """
    Функция принимает строку пользователя с данными
    и приводит ее к стандартному зашифрованному виду.
    :param user_input: строка с данными
    # :return: Карта|Счет, номер карты|счета
    """
    split_str = user_input.split(" ")
    if len(split_str[-1]) == 16:
        return f"{' '.join(split_str[:len(split_str) - 1])} {card_encryption(split_str[-1])}"
    elif len(split_str[-1]) == 20:
        return f"{' '.join(split_str[0:len(split_str) - 1])} {account_encryption(split_str[-1])}"
    else:
        return "Неверный номер счета или карты"


def data_fix(user_input: str) -> str:
    """
    Функция получает от пользователя строку с информацией
    даты и времени, и возвращает дату.
    :param user_input: пользователь вводит дату и время
    :return: день.месяц.год
    """
    the_data = datetime.fromisoformat(user_input)
    return the_data.strftime("%d.%m.%Y")
