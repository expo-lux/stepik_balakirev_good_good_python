# s = input().split()
s = "Москва 15000 Уфа 1200 Самара 1090 Казань 1300".split()
lst = [[s[i], int(s[i+1])] for i in range(0, len(s), 2)]
print(lst)
