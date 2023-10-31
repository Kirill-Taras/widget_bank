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
        return sorted(data, key=lambda x: x['date'], reverse=True)
    if not reverse:
        return sorted(data, key=lambda x: x['date'])
