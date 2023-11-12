from datetime import datetime
from functools import wraps
from typing import Callable, Any


def log(filename: None | str = None) -> Callable:
    def wrapped(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            now: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result: Any = function(*args, **kwargs)
                log_messenger: str = f"{now} {function.__name__} ok\n"
            except Exception as err:
                result: None = None
                log_messenger: str = (
                    f"{now} {function.__name__} " f"error: {type(err).__name__}. " f"Inputs: {args}, {kwargs}\n"
                )
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_messenger)
            else:
                print(log_messenger)
            return result

        return inner

    return wrapped
