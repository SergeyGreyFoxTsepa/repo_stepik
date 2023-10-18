"""Что бы линтер не ругался что нет описания)"""


def get_string(string: str, times: int, sep: str = '') -> str:
    """Комиттить переменные в функции, что бы линтер понимал что будет в
    функции"""
    return sep.join([string] * times)


get_string('World', 56)
