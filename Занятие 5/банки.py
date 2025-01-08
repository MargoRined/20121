n = int(input('Введите количество банков: '))
m = []
w = 0
y2 = []
for _ in range(n):
    b = input('Введите имя банка: ')
    d = int(input('Введите сумму денег: '))
    e = int(input('Введите порядковый номер банка: '))
    m1 = (b, d, e)
    m.append(m1)
for i, j, k in m:
    for g, h, t in m:
        if abs(k - t) > 1:
            y = ((j + h), (i, k), (g, t))
            y2.append(y)
for i, j, u in y2:
    w = max(i, w)
for i, j, u in y2:    
    if i == w:
        print([i, j, u])
        break
    else:
        continue