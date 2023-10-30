def get_data(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей
    и значение для ключа state, и возвращает новый список,
    содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение.
    :param data: list[dict]
    :param state: str
    :return: list[dict]
    """
    list_data: list = list()
    for data_state in data:
        if data_state["state"] == state:
            list_data.append(data_state)
    return list_data


def get_data_by_date(data: list[dict], gradation: str = "убывание") -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты.
    :param data: list[dict]
    :param gradation: str
    :return: list[dict]
    """
    if gradation == "убывание":
        return sorted(data, key=lambda x: x['date'], reverse=True)
    if gradation == "возрастание":
        return sorted(data, key=lambda x: x['date'])
