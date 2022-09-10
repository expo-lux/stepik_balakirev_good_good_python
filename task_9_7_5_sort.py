# Номер;Имя;Оценка;Зачет -> #Имя;Зачет;Оценка;Номер
# lst_in = ['Номер;Имя;Оценка;Зачет', '3;Портс;5;Да', '1;Портос;5;Да', '5;Балакирев;1;Нет']

s = ["Номер;Имя;Оценка;Зачет",
     "1;Портос;5;Да",
     "2;Арамис;3;Да",
     "3;Атос;4;Да",
     "4;д'Артаньян;2;Нет",
     "5;Балакирев;1;Нет"]

lst_in = list(map(str.strip, s))


def parse_l(line):
    number_, name_, mark_, passed_ = line.split(';')
    return name_, passed_, int(mark_), int(number_)


number, name, mark, passed = lst_in[0].split(';')
header = name, passed, mark, number
t = tuple(map(parse_l, lst_in[1:]))
l = sorted(t, key=lambda item: item[-1])
l.insert(0, header)
t_sorted = tuple(l)
print(t_sorted)
