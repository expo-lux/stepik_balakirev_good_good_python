x = iter("Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь".split())


print(next(x))
for i in zip(x, x, x):
    print(*i)