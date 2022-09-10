def print_top_elements_oneline(n: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for counter, value in enumerate(func(*args, **kwargs), 1):
                if counter > n:
                    break
                print(value, end=' ')
        return wrapper
    return decorator

@print_top_elements_oneline(20)
def primes():
    val = 2
    while True:
        simple = True
        for i in range(2, val):
            if val % i == 0:
                simple = False
                break
        if simple:
            yield val
        val += 1

primes()