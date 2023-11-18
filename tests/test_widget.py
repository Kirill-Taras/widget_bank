import pytest

from src.widget import card_type_number, data_fix


@pytest.mark.parametrize(
    "data, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa 123456", "Неверный номер счета или карты"),
    ],
)
def test_card_type_number(data: str, expected_result: str) -> None:
    assert card_type_number(data) == expected_result


@pytest.mark.parametrize(
    "data_time, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_data_fix(data_time: str, expected_result: str) -> None:
    assert data_fix(data_time) == expected_result
