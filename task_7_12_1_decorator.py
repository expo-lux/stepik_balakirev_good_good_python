def add(start: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + start
        return wrapper
    return inner

@add(5)
def summ(s: str) -> int:
    l = list(map(int, s.split()))
    return sum(l)

if __name__ == '__main__':
    s = '5 6 3 6 -4 6 -1'
    print(summ(s))