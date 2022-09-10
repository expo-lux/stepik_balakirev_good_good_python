from functools import wraps


def summator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args, **kwargs))
    return wrapper

@summator
def get_list(s: str) -> list:
    """Функция для формирования списка целых значений"""
    return list(map(int, s.split()))


s = '1 2 3 4 5'
print(get_list.__doc__)
print(get_list.__name__)
print(get_list(s))