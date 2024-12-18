def deal(n: list, s: int, p: int, h: str, i: int):
    ''' Функция для + или - чисел, чтобы проверить равна ли их сумма-разность заданному финальному числу'''
    if i == len(n):
        if p == a[-1]:
            return h[:-1]
        else:
            return None
    x = deal(n, s, p + n[i], str(h) + '+' + str(n[i]), i + 1)
    y = deal(n, s, p - n[i], str(h) + '-' + str(n[i]), i + 1)
    return x or y
with open("1.txt", "r") as file:
    a = list(map(int, file.read().split()))
g = deal(a[1:-1], a[-1], 0, '', 0)
with open("2.txt", "w") as file:
    if g:
        file.write(str(g[3:]) + '=' + str(a[-1]))
    else:
        file.write("no solution")
