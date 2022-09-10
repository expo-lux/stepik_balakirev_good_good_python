# put your python code here
n = int(input())
i, summa = 1, 0
while i <= n:
    summa += 1/i
    i += 1
print(f"{summa:.3f}")