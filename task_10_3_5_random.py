import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]
count = 0
for i in range(0, N, 2):
    if count >= 10:
        break
    for j in range(0, N, 2):
        P[i][j] = 1
        count +=1
        if count >= 10:
            break