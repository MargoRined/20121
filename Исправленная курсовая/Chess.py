import ast
from Kursovaya import Wrong_koordinates, AnotherWindow, MainWindow
from PySide6.QtWidgets import QLineEdit
import itertools
class Chess(object):
    ''' Класс для работы с шахматами'''
    W = []
    W1 = []
    W2 = []
    W2_2 = []
    lineEdit_list = []
    all_field_boxes = []
    _list = []
    listing = []

    def __init__(self):
        ''' Вводная функция'''
        self.open_window = []
        self.all_field_boxes = []
        self.line_edit = QLineEdit()
        self.line_edit_1 = QLineEdit()
        self.line_edit_2 = QLineEdit()

    def good_bad_koordinats(self):
        ''' Функция для записи данных в файл с главного окна'''
        with open('input.txt', 'r') as file:
            f = file.readlines()
            N, L, K = map(int, f[0].strip().split())
            if f[0].count(' ') == 2:
                with open('output.txt', 'w') as file:
                    file.write(f'{N} {L} {K}\n')
            if f[0].count(' ') < 2:
                pass
        return N, L, K

    def koordinats_giving(self):
        ''' Функция для записи введенных координат в файл input'''
        with open('output.txt', 'r') as file:
            f = file.readline()
            N1, L1, K1 = map(int, f.strip().split())
            listing = []
            _list = [lineEdit.text() for lineEdit in Chess.lineEdit_list]
            if (len(_list) == K1) and ('' not in _list):
                for j in _list:
                    k = 0
                    for i in range(len(j)):
                        if j[i] == ' ':
                            k += i
                            listing.append((str(int(j[0:k]) - 1) + ' ' + str(int(j[k + 1:]))))
                            listing.append((str(int(j[0:k]) + 1) + ' ' + str(int(j[k + 1:]))))
                            listing.append((str(int(j[0:k]) + 1) + ' ' + str(int(j[k + 1:]) + 2)))
                            listing.append((str(int(j[0:k]) - 1) + ' ' + str(int(j[k + 1:]) + 2)))
                            listing.append((str(int(j[0:k]) - 1) + ' ' + str(int(j[k + 1:]) - 2)))
                            listing.append((str(int(j[0:k]) + 1) + ' ' + str(int(j[k + 1:]) - 2)))

                with open('input.txt', 'w') as f:
                    f.write(f'{N1} {L1} {K1}\n')
                    for k in _list:
                        if k in listing:
                            error = Wrong_koordinates()
                            error.show()
                            self.open_window.append(error)
                            _list.remove(k)
                        if len(_list) == K1:
                            f.write(f'{k}\n')

    def solutions(self):
        ''' Функция для записи решеений в файл output'''
        with open('output.txt', 'w'):
            pass
        figure_stay = []
        figure_stay_go = []
        f_f = []
        with open('input.txt', 'r') as file:
            f = file.readlines()
            N2, L2, K2 = map(int, f[0].strip().split())
            for i in f[1:]:
                k = 0
                for j in range(len(i)):
                    if i[j] == ' ':
                        k += j
                        f_f.append((int(i[0:k]), int(i[k + 1:])))
                        figure_stay.append((int(i[0:k]), int(i[k + 1:])))
                        if int(i[k + 1:]) - 1 >= 0:
                            f_f.append((int(i[0:k]), int(i[k + 1:]) - 1))
                            figure_stay_go.append((int(i[0:k]), int(i[k + 1:]) - 1))
                        f_f.append((int(i[0:k]), int(i[k + 1:]) + 1))
                        figure_stay_go.append((int(i[0:k]), int(i[k + 1:]) + 1))
                        if int(i[0:k]) - 2 >= 0:
                            f_f.append((int(i[0:k]) - 2, int(i[k + 1:]) + 1))
                            figure_stay_go.append((int(i[0:k]) - 2, int(i[k + 1:]) + 1))
                        if int(i[0:k]) - 2 >= 0 and int(i[k + 1:]) - 1 >= 0:
                            f_f.append((int(i[0:k]) - 2, int(i[k + 1:]) - 1))
                            figure_stay_go.append((int(i[0:k]) - 2, int(i[k + 1:]) - 1))
                        if int(i[k + 1:]) - 1 >= 0:
                            f_f.append((int(i[0:k]) + 2, int(i[k + 1:]) - 1))
                            figure_stay_go.append((int(i[0:k]) + 2, int(i[k + 1:]) - 1))
                        f_f.append((int(i[0:k]) + 2, int(i[k + 1:]) + 1))
                        figure_stay_go.append((int(i[0:k]) + 2, int(i[k + 1:]) + 1))

        Chess.all_field_boxes = [(y, x) for y in range(N2) for x in range(N2)]

        free_field_boxes = [(i[1], i[0]) for i in (set(Chess.all_field_boxes) - set(f_f))]

        with open('output.txt', 'w') as file_1:
            all_varients = []
            all_combinations = itertools.combinations(free_field_boxes, L2)
            for i in all_combinations:
                all_varients.append(i)
            if len(all_varients) > 0:
                for i in all_varients:
                    while len(i) > 0:
                        z = []
                        for j in range(len(i)):
                            if (int(i[j][0]) - 1, int(i[j][1])) in i: z.append((int(i[j][0]) - 1, int(i[j][1])))
                            if (int(i[j][0]) + 1, int(i[j][1])) in i: z.append((int(i[j][0]) + 1, int(i[j][1])))
                            if (int(i[j][0]) + 1, int(i[j][1]) - 2) in i: z.append((int(i[j][0]) + 1, int(i[j][1]) - 2))
                            if (int(i[j][0]) - 1, int(i[j][1]) - 2) in i: z.append((int(i[j][0]) - 1, int(i[j][1]) - 2))
                            if (int(i[j][0]) - 1, int(i[j][1]) + 2) in i: z.append((int(i[j][0]) - 1, int(i[j][1]) + 2))
                            if (int(i[j][0]) + 1, int(i[j][1]) + 2) in i: z.append((int(i[j][0]) + 1, int(i[j][1]) + 2))
                        if len(list(set(i) - set(z))) == L2:
                            for p in figure_stay:
                                file_1.write(str(p[::-1]) + ' ')
                            for p1 in list(set(i) - set(z)):
                                file_1.write(str(p1) + ' ')
                            file_1.write('\n')
                        break
            else:
                file_1.write("No solutions!")

    def table_koord(self):
        ''' Функция для записи данных в списки для шахматной доски'''
        with open('output.txt', 'r') as file_4:
            with open('input.txt', 'r') as file_3:
                f1 = file_4.readlines()
                f = file_3.readlines()
                N3, L3, K3 = map(int, f[0].strip().split())
                if ('No solutions!'  not in f1) and (str(N3) != ' '):
                    K_K = [(-1, 0), (1, 0), (1, -2), (-1, -2), (-1, 2), (1, 2)]
                    f12 = f1[0].replace(') (', ')*(').split('*')
                    l = [ast.literal_eval(i) for i in f12]
                    for i in set(l[0:K3]):
                        for j in set(K_K):
                            Chess.W.append(i)
                            Chess.W1.append((int(i[0]) + int(j[0]), int(i[1]) + int(j[1])))
                    for i in set(l[K3:]):
                        for j in set(K_K):
                            Chess.W2.append(i)
                            Chess.W1.append((int(i[0]) + int(j[0]), int(i[1]) + int(j[1])))
                for i in set(Chess.all_field_boxes):
                    if (i not in Chess.W) and (i not in Chess.W2) and (i not in Chess.W1):
                        Chess.W2_2.append(i)
        return Chess.W, Chess.W2, Chess.W1, Chess.W2_2

if __name__ == '__main__':
    N, L, K = Chess.good_bad_koordinats
    Chess.solutions()
    Chess.koordinats_giving()
    Chess.W, Chess.W2, Chess.W1, Chess.W2_2 = Chess.table_koord
