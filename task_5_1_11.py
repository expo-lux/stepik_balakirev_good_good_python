# put your python code here
n, i = int(input()), 0
s = 1000
while i < n:
    s *= 1.05
    i += 1
s = f"{s:.2f}"
s = s if s[-1] != '0' else s[0:-1]
print(f"{s}")
