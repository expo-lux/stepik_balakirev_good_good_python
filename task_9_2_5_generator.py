import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)

def print_top_elements(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for counter, value in enumerate(func(*args, **kwargs), 1):
                if counter > n:
                    break
                print(value)
        return wrapper
    return decorator

@print_top_elements(5)
def gen_email(pass_len: int):
    chars = ascii_lowercase + ascii_uppercase
    while True:
        username = [chars[random.randint(0, len(chars))]
                    for i in range(pass_len)]
        yield ''.join(username) + '@mail.ru'

n = int(input())
gen_email(n)