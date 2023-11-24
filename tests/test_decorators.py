import os
from datetime import datetime
from typing import Any

import pytest

from src.config import TEST_MYLOG_PATH
from src.decorators import log


@pytest.mark.parametrize(
    "arg1, arg2, expected",
    [
        (2, 0, " foo error: ZeroDivisionError. Inputs: (2, 0), {}"),
        (2, "2", " foo error: TypeError. Inputs: (2, '2'), {}"),
        (10, 5, " foo ok"),
    ],
)
def test_log(arg1: str | int, arg2: str | int, expected: str) -> None:
    if TEST_MYLOG_PATH.exists():
        os.remove(TEST_MYLOG_PATH)

    @log(TEST_MYLOG_PATH)
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg1, arg2)

    with open(TEST_MYLOG_PATH) as file:
        log_messenger = file.read().strip()

    expected_log = now + expected

    assert log_messenger == expected_log


@pytest.mark.parametrize(
    "arg1, arg2, expected",
    [
        (2, 0, " foo error: ZeroDivisionError. Inputs: (2, 0), {}"),
        (2, "2", " foo error: TypeError. Inputs: (2, '2'), {}"),
        (10, 5, " foo ok"),
    ],
)
def test_log_console(arg1: str | int, arg2: str | int, expected: str, capsys: Any) -> None:
    @log()
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg1, arg2)

    expected_log = now + expected

    log_messenger = capsys.readouterr()

    assert expected_log == log_messenger.out.strip()
