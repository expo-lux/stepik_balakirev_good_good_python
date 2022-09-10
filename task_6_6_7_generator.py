lst_in = ["Пушкин: Сказака о рыбаке и рыбке",
          "Есенин: Письмо к женщине",
          "Тургенев: Муму",
          "Пушкин: Евгений Онегин",
          "Есенин: Русь"]

# lst_in, d = list(map(str.strip, sys.stdin.readlines())), {}
d = {}
for item in lst_in:
    key = item.split(":")[0]
    value = item.split(":")[1].strip()
    if key in d:
        d[key].add(value)
    else:
        d[key] = set([value])
print(d)
{item.split(":")[0]: item.split(":")[1].strip() for item in lst_in}