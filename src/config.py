from pathlib import Path

ROOT_PATH = Path(__file__).parent  # путь к директории src
MYLOG_PATH = Path.joinpath(ROOT_PATH.parent, "data", "mylog.txt")  # путь к лог-файлу
TEST_MYLOG_PATH = Path.joinpath(ROOT_PATH.parent, "data", "test_mylog.txt")  # путь к тестовому лог-файлу
OPERATIONS_PATH = Path.joinpath(ROOT_PATH.parent, "data", "operations.json")  # путь к файлу json с тразакциями
TEST_JSON_PATH = Path.joinpath(ROOT_PATH.parent, "data", "test_operations.json")  # путь к тест-файлу json
LOG_MASKS = Path.joinpath(ROOT_PATH.parent, "data", "log_masks.log")
LOG_UTILS = Path.joinpath(ROOT_PATH.parent, "data", "log_utils.log")
