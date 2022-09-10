def make_dict(func):
    def wrapper(*args, **kwargs):
        return dict(zip(*func(*args, **kwargs)))
    return wrapper

@make_dict
def make_list(*args):
    return [_.split() for _ in args]

d = make_list("house river tree car", "дом река дерево машина")
print(*sorted(d.items()))