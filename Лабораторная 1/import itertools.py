def deal(n: list, s: int, p: int = 0, h: str = "", i: int = 0):
    ''' Функция для + или - чисел, чтобы проверить равна ли их сумма-разность заданному финальному числу '''
    if i == len(n):
        if p == s:
            return h[:-1]
        else:
            return None
    x = deal(n, s, p + n[i], f"{h} + {n[i]} ", i + 1)
    y = deal(n, s, p - n[i], f"{h} - {n[i]} ", i + 1)
    return x or y
with open("1.txt", "r") as file:
    a = list(map(int, file.read().split()))
g = deal(a[1:-1], a[-1])
with open("2.txt", "w") as file:
    if g is not None:
        file.write(f"{g[3:]} = {a[-1]}")
    else:
        file.write("No solution")