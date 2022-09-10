def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

def get_rec_sum(l):
    if len(l):
        return l[-1] + get_rec_sum(l[:len(l)-1])
    else:
        return 0


print(fac(5))
x = [1,0,0,0,0,1]

# it = iter(x)
# print(next(it))
print(get_rec_sum(x))
