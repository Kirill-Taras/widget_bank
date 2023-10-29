def card_encryption(number_card: str) -> str:
    """
    Функция принимает номер карты пользователя
    и возвращает его зашифрованный вид.
    :param number_card: номер карты пользователя
    :return: str
    """
    encoded_number_card = number_card[0:6] + "******" + number_card[-4:]
    split_number_card = [encoded_number_card[i:i + 4] for i in range(0, len(number_card), 4)]
    return " ".join(split_number_card)


def account_encryption(account_number: str) -> str:
    """
    Функция принимает номер счета пользователя
    и возвращает его зашифрованный вид.
    :param account_number: номер счета пользователя
    :return: str
    """
    return "**" + account_number[-4:]
