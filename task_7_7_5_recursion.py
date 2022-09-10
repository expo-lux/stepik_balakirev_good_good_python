# ввод числа N
# N = int(input())

def sumtree(l: list):
    total = 0
    for x in l:
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total


def fib_rec(n, f=[]):
    if n > len(f):
        if n <= 2:
            f += [1, 1]
        else:
            fib_rec(n - 1)
            f.append(f[-2] + f[-1])
    return f[: n]


def fib_rec_wrong(n: int, f: list = []):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    else:
        return [*fib_rec(n - 1), fib_rec(n - 1)[-1] + fib_rec(n - 1)[-2]]


# for i in range(1, 20):
#     print(f"{i}:", *fib_rec(i))
print(fib_rec(4))
l = [1, [2, [[3,4],5], 6, [7,8]]]
print(sumtree(l))
