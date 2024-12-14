def number(Nu):
    u = 0
    p = 0 # предыдущее значение в числе
    d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    for i in reversed(Nu):
        value = d[i]
        if value > p:
            u += value
        else:
            u -= value
        p = value
    return u
o = number('LIV')
print(o)