import itertools 
def read(name1): 
    ''' Функция для считывания данных из файла '''
    with open(name1, 'r') as file: 
        a = file.readline().strip().split() 
    return a 
def deal(a): 
    ''' Функция для формирования комбинций цифр и знаков и проверки суммы '''
    O = itertools.product([i for i in a[1:-1]], ['+', '-'], repeat = len([i for i in a[1:-1]])) 
    V = [i[:-1] for i in O if list(i[::2]) == a[1:-1]] 
    h = [] 
    for i in V: 
        p = 0
        p += int(i[0]) 
        for j in range(len(i)-1): 
            if i[j] == '-': 
                p -= int(i[j+1]) 
            elif i[j] == '+': 
                p += int(i[j+1]) 
        h.append([p, i]) 
        p == 0 
    h1 = [k[1] for k in h if str(k[0]) == str(a[-1])]
    if len(h1) > 0:
        print(*h1.pop(), '=', a[-1])
    else:
        print('No solution')
def main(): 
    ''' Функция для работы со всеми функциями '''
    a = read('1.txt') 
    deal(a) 
if __name__ == '__main__': 
    ''' Запуск главной функции '''
    main() 
