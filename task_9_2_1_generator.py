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


print(type(primes()))


def genf():
    s = """1234
12345678910
    """
    s.rjust()
    print(s)


genf()


# gen = genf()
# for i in genf():
#     print(i)
#     if i == 5:
#         break
#
# for i in gen:
#     print(i)
#     if i == 5:
#         break
# min()

