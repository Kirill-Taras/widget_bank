import os

import pytest

from src.config import MYLOG_PATH, TEST_JSON_PATH, OPERATIONS_PATH, CSV_FILE, XLSX_FILE
from src.utils import get_json_file, get_operations, get_file


@pytest.fixture()
def operation() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


@pytest.mark.parametrize(
    "file, expected",
    [
        (
            TEST_JSON_PATH,
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
        (MYLOG_PATH, []),
        ("file.json", []),
    ],
)
def test_get_json_file(file: str, expected: list) -> None:
    json_file = get_json_file(file)
    assert json_file == expected


def test_get_operations(operation: list[dict]) -> None:
    with pytest.raises(ValueError):
        get_operations(operation[1])
    assert get_operations(operation[0]) == 31957.58


@pytest.mark.parametrize(
    "file, expected",
    [(OPERATIONS_PATH, 441945886), (CSV_FILE, 650703), (XLSX_FILE, 650703)])
def test_get_file(file, expected):
    result = get_file(file)
    if ".json" in os.path.basename(file):
        assert result[0]["id"] == expected
    elif ".csv" or ".xlsx" in os.path.basename(file):
        assert result["id"][0] == expected
