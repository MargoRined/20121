import itertools

def read_file(name : any): 
    ''' Функция считывания данных из файла '''
    with open(name, 'r') as file: 
        f = file.readlines()  
        N, L, K = map(int, f[0].strip().split()) 
        G = [f[i].strip().split() for i in range(1, K+1)] 
    return N, L, G, K 

def figure(G:list[int]): 
    ''' Функция считывания данных фигуры, уже стоящей на доске '''
    U = [] 
    E = [] 
    for i in G:
        U.append((int(i[1]), int(i[0])))
        U.append((int(i[1])-1, int(i[0])))
        U.append((int(i[1])+1, int(i[0])))
        U.append((int(i[1])+1, int(i[0])-2))
        U.append((int(i[1])-1, int(i[0])-2))
        U.append((int(i[1])-1, int(i[0])+2))
        U.append((int(i[1])+1, int(i[0])+2))
        E.append((int(i[1]), int(i[0])))
    return U, E

def another(U: list[int]): 
    ''' Функция координат фигуры и её ходов '''
    U1 = []
    U2 = []
    for i in U: 
        for j in i:
            if j < 0: 
                U1.append(i)
            else: 
                U2.append(i)
    U3 = set(U2) - set(U1) 
    return U3

def step(N : int): 
    ''' Функция всех клеток шахматной доски '''
    H = [(y, x) for y in range(N) for x in range(N)] 
    return set(H) 

def right(H: set[int], U: list[int]): 
    ''' Функция для клеток, куда можно поставить фигуры '''
    H1 = [(i[0], i[1]) for i in (set(H) - set(U))] 
    return set(H1) 

def write(name1: any, L: int, H1: set[int], E: list[int]): 
    ''' Функция для записи координат в файл '''
    B = [] 
    A = []
    N1 = itertools.combinations(H1, L) 
    for i in N1:
        B.append(i) 
    with open(name1, 'w') as ko: 
        if len(B) > 0:
            for i in B:
                while len(i) > 0: 
                    z = []
                    for j in range(len(i)): 
                        if (int(i[j][0])-1, int(i[j][1])) in i: z.append((int(i[j][0])-1, int(i[j][1])))
                        if (int(i[j][0])+1, int(i[j][1])) in i: z.append((int(i[j][0])+1, int(i[j][1])))
                        if (int(i[j][0])+1, int(i[j][1])-2) in i: z.append((int(i[j][0])+1, int(i[j][1])-2))
                        if (int(i[j][0])-1, int(i[j][1])-2) in i: z.append((int(i[j][0])-1, int(i[j][1])-2))
                        if (int(i[j][0])-1, int(i[j][1])+2) in i: z.append((int(i[j][0])-1, int(i[j][1])+2))
                        if (int(i[j][0])+1, int(i[j][1])+2) in i: z.append((int(i[j][0])+1, int(i[j][1])+2))
                    A.append((set(i) - set(z)))
                    if len(list(set(i) - set(z))) == L:
                        for p in E: 
                            ko.write(str(p[::-1]) + ' ')
                        for p1 in list(set(i) - set(z)):
                            ko.write(str(p1) + ' ')
                        ko.write('\n') 
                    break
        else: 
            ko.write('No solution') 
    return A     

def board(N: int, U3: set[int], E: list[int], A: list[int]):
    ''' Функция вывода шахматной доски в консоль '''
    d = [[(y, x) for y in range(N)] for x in range(N)]
    W = []
    W1 = []
    for j in A[0]:
        W1.append((j[0], j[1]))
        W.append((int(j[0]) - 1, int(j[1])))
        W.append((int(j[0]) + 1, int(j[1])))
        W.append((int(j[0]) + 1, int(j[1]) - 2))
        W.append((int(j[0]) - 1, int(j[1]) - 2))
        W.append((int(j[0]) - 1, int(j[1]) + 2))
        W.append((int(j[0]) + 1, int(j[1]) + 2))
    for i in d: 
        h = [] 
        for j in i: 
            if (j in E) or (j in W1): 
                h.append('#') 
            elif (j in U3) or (j in W): 
                h.append('*')
            else: 
                h.append('0') 
        print(*[i for i in h if i in '0*#'])

def main(): 
    ''' Функция для работы со всеми функциями '''
    N, L, G, K = read_file('1.txt') 
    U, E = figure(G)
    H = step(N) 
    H1 = right(H, U) 
    U3 = another(U)
    A = write('2.txt', L, H1, E)
    board(N, U3, E, A) 
     
if __name__ == '__main__': 
    ''' Приводим в действие самую главную функцию '''
    main() 
