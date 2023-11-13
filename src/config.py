from pathlib import Path

ROOT_PATH = Path(__file__).parent  # путь к директории src
MYLOG_PATH = Path.joinpath(ROOT_PATH.parent, "data", "mylog.txt")  # путь к лог-файлу
TEST_MYLOG_PATH = Path.joinpath(ROOT_PATH.parent, "data", "test_mylog.txt")  # путь к тестовому лог-файлу
