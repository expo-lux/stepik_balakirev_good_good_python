# def merge_sort(orig: list):
#     def merge(L: list, R: list):
#         C = [0] * (len(L) + len(R))
#         i = k = n = 0
#         while i < len(L) and k < len(R):
#             if L[i] <= R[k]:
#                 C[n] = L[i]
#                 i += 1
#             else:
#                 C[n] = R[k]
#                 k += 1
#             n += 1
#         while i < len(L):
#             C[n] = L[i]
#             n += 1
#             i += 1
#         while k < len(R):
#             C[n] = R[k]
#             n += 1
#             k += 1
#         return C
#
#     middle = len(orig) // 2
#     if len(orig) <= 1:
#         return
#     l, r = orig[:middle], orig[middle:]
#     merge_sort(l)
#     merge_sort(r)
#     C = merge(l, r)
#     orig[:] = C[:]

def merge_sort(orig: list):
    def merge(L: list, R: list):
        C = [0] * (len(L) + len(R))
        i = k = n = 0
        while i < len(L) and k < len(R):
            if L[i] <= R[k]:
                C[n] = L[i]
                i += 1
            else:
                C[n] = R[k]
                k += 1
            n += 1
        while i < len(L):
            C[n] = L[i]
            n += 1
            i += 1
        while k < len(R):
            C[n] = R[k]
            n += 1
            k += 1
        return C

    middle = len(orig) // 2
    if len(orig) <= 1:
        return orig
    l, r = orig[:middle], orig[middle:]
    l = merge_sort(l)
    r = merge_sort(r)
    C = merge(l, r)
    return C


lst = [int(i) for i in '8 11 -6 3 0 1 1'.split()]
sorted_l = merge_sort(lst)
print(*sorted_l)