# put your python code here
n = int(input())
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
t2 = tuple([t[i][:n] for i in range(n)])
for row in t2:
    print(*row)