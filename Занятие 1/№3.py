def zigzag(m, n):
    if n == 1:
        return m #если строка одна, то возвращаем слово
    rs = [''] * n #создаём список строк для подстрок zigzag
    l, step = 0, 1
    for k in m:
        rs[l] += k #добавляем букву из слова в строку
        if l == 0: #если верхняя или нижняя строка, то меняем направление хода
            step = 1
        elif l == n - 1: #идём зигзагом по строкам
            step = -1
        l += step
    return "".join(rs) #объединем строки в одну
m = input("") #вводим слово
n = int(input()) #вводим количество строк
print(zigzag(m, n))