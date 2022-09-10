import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
lst_out = [col
           for row in lst_in
           for col in row
           ]

print(*lst_out)
