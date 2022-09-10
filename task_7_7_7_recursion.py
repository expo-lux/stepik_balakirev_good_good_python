d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

def get_line_list(d,a=[]):
    for x in d:
        if not isinstance(x, list):
            a.append(x)
        else:
            get_line_list(x, a)
    return a


print(get_line_list(d))