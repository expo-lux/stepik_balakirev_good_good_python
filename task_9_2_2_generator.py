def get_sum(n: int):
    for i in range(1,n+1):
        yield sum(range(i+1))


def gen1():
    i = 0
    s = '121'
    # while True:
    x = s + '1'
    yield x

k = 1
for i in gen1():
    print(i)
    if k == 4:
        break
    k += 1


for i in range(5):
    print(next(gen1()))

