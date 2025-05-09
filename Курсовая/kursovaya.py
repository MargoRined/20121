import itertools
import sys
from PySide6.QtWidgets import QLineEdit, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow, QGridLayout, QTableWidget, QTableWidgetItem

class Wrong_koordinates(QMainWindow):
    ''' Класс для создания окна при вводе неправильных координат фигур'''
    def __init__(self):
        ''' Начальная функция для декорирования окна'''
        super().__init__()
        self.setWindowTitle("Error")
        self.resize(100, 100)
        central = QWidget()
        self.setCentralWidget(central)

        self.label = QLabel("Были введены координаты под ударом. Координаты не будут записаны в файл.")

        self.button = QPushButton("Exit")
        self.button.clicked.connect(self.on_button_cl)

        self.layout = QVBoxLayout(central)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

    def on_button_cl(self):
        ''' Функция для кнопки закрытия'''
        Wrong_koordinates.deleteLater(self)

class AnotherWindow(Wrong_koordinates):
    ''' Класс для окна с вводом координат и записью данных в файл input'''
    def __init__(self):
        ''' Первоначальная функция для декорирования окна'''
        super().__init__()
        self.setWindowTitle("Adding window")
        self.resize(695, 533)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.open_window = []

        self.lineEdit_list = []

        with open('output.txt', 'r') as file:
            f = file.readline()
            N, L, K = map(int, f.strip().split())

        if K > 1:
            count_K = 0
            for i in range(1, K):
                for j in range(0, K):
                    while count_K < K:
                        self.line_edit = QLineEdit()
                        self.lineEdit_list.append(self.line_edit)
                        self.layout.addWidget(self.line_edit, i, j)
                        count_K += 1
                        break
        else:
            self.line_edit = QLineEdit()
            self.lineEdit_list.append(self.line_edit)
            self.layout.addWidget(self.line_edit, 0, 0)

        self.label = QLabel()
        self.button = QPushButton("enter")
        self.button_1 = QPushButton("exit")
        self.button.clicked.connect(self.get_1)
        self.button_1.clicked.connect(self.on_button_click)

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.widget)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.button_1)

    def get_1(self):
        ''' Функция для записи данных в файл input при нажатии на кнопку'''
        with open('output.txt', 'r') as file:
            f = file.readline()
            N, L, K = map(int, f.strip().split())
        with open('input.txt', 'w') as file:
            file.write(f'{N} {L} {K}\n')
            listing = []
            _list = [lineEdit.text() for lineEdit in self.lineEdit_list]
            if (len(_list) == K) and ('' not in _list):
                for j in _list:
                    if j[1] == ' ':
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2]))))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2]))))
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2]) + 2)))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2]) + 2)))
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2]) - 2)))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2]) - 2)))
                    elif (j[1] == ' ') and (j[3] in '0123456789'):
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2:4]))))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2:4]))))
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2:4]) + 2)))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2:4]) + 2)))
                        listing.append((str(int(j[0]) - 1) + str(' ') + str(int(j[2:4]) - 2)))
                        listing.append((str(int(j[0]) + 1) + str(' ') + str(int(j[2:4]) - 2)))
                    elif (j[1] != ' '):
                         listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3]))))
                         listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3]))))
                         listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3]) + 2)))
                         listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3]) + 2)))
                         listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3]) - 2)))
                         listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3]) - 2)))
                    elif (j[1] != ' ') and (j[4] in '0123456789'):
                        listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3:5]))))
                        listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3:5]))))
                        listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3:5]) + 2)))
                        listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3:5]) + 2)))
                        listing.append((str(int(j[0:2]) - 1) + str(' ') + str(int(j[3:5]) - 2)))
                        listing.append((str(int(j[0:2]) + 1) + str(' ') + str(int(j[3:5]) - 2)))

                with open('input.txt', 'w') as f:
                    f.write(f'{N} {L} {K}\n')
                    for k in _list:
                        if k in listing:
                            error = Wrong_koordinates()
                            error.show()
                            self.open_window.append(error)
                            _list.remove(k)
                        if len(_list) == K:
                            f.write(f'{k}\n')


    def on_button_click(self):
        ''' Функция для кнопки закрытия окна'''
        AnotherWindow.deleteLater(self)

class Window(QWidget):
    ''' Класс для создания шахматной доски и записи координат'''
    def __init__(self):
        ''' Начальная функция создания окна'''
        super().__init__()
        self.setWindowTitle("Chess Board")
        self.resize(695, 533) #размер окна с таблицей
        self.create_table()
        self.show()


    def create_table(self):
        ''' Функция создание табличного шахматного поля и записи координат в файл '''
        figure_stay = []
        figure_stay_go = []
        f_f = []
        with open('input.txt', 'r') as file:
            f = file.readlines()
            N, L, K = map(int, f[0].strip().split())
            for i in f[1:]:
                if i[1] == ' ':
                    f_f.append((int(i[0]), int(i[2])))
                    f_f.append((int(i[0]), int(i[2]) - 1))
                    f_f.append((int(i[0]), int(i[2]) + 1))
                    f_f.append((int(i[0]) - 2, int(i[2]) + 1))
                    f_f.append((int(i[0]) - 2, int(i[2]) - 1))
                    f_f.append((int(i[0]) + 2, int(i[2]) - 1))
                    f_f.append((int(i[0]) + 2, int(i[2]) + 1))

                    figure_stay.append((int(i[0]), int(i[2])))
                    figure_stay_go.append((int(i[0]), int(i[2]) - 1))
                    figure_stay_go.append((int(i[0]), int(i[2]) + 1))
                    figure_stay_go.append((int(i[0]) - 2, int(i[2]) + 1))
                    figure_stay_go.append((int(i[0]) - 2, int(i[2]) - 1))
                    figure_stay_go.append((int(i[0]) + 2, int(i[2]) - 1))
                    figure_stay_go.append((int(i[0]) + 2, int(i[2]) + 1))
                elif (i[1] == ' ') and (i[3] in '0123456789'):
                    f_f.append((int(i[0]), int(i[2:4])))
                    f_f.append((int(i[0]), int(i[2:4]) - 1))
                    f_f.append((int(i[0]), int(i[2:4]) + 1))
                    f_f.append((int(i[0]) - 2, int(i[2:4]) + 1))
                    f_f.append((int(i[0]) - 2, int(i[2:4]) - 1))
                    f_f.append((int(i[0]) + 2, int(i[2:4]) - 1))
                    f_f.append((int(i[0]) + 2, int(i[2:4]) + 1))

                    figure_stay.append((int(i[0]), int(i[2:4])))
                    figure_stay_go.append((int(i[0]), int(i[2:4]) - 1))
                    figure_stay_go.append((int(i[0]), int(i[2:4]) + 1))
                    figure_stay_go.append((int(i[0]) - 2, int(i[2:4]) + 1))
                    figure_stay_go.append((int(i[0]) - 2, int(i[2:4]) - 1))
                    figure_stay_go.append((int(i[0]) + 2, int(i[2:4]) - 1))
                    figure_stay_go.append((int(i[0]) + 2, int(i[2:4]) + 1))
                elif (i[1] != ' '):
                    f_f.append((int(i[0:2]), int(i[3])))
                    f_f.append((int(i[0:2]), int(i[3]) - 1))
                    f_f.append((int(i[0:2]), int(i[3]) + 1))
                    f_f.append((int(i[0:2]) - 2, int(i[3]) + 1))
                    f_f.append((int(i[0:2]) - 2, int(i[3]) - 1))
                    f_f.append((int(i[0:2]) + 2, int(i[3]) - 1))
                    f_f.append((int(i[0:2]) + 2, int(i[3]) + 1))

                    figure_stay.append((int(i[0:2]), int(i[3])))
                    figure_stay_go.append((int(i[0:2]), int(i[3]) - 1))
                    figure_stay_go.append((int(i[0:2]), int(i[3]) + 1))
                    figure_stay_go.append((int(i[0:2]) - 2, int(i[3]) + 1))
                    figure_stay_go.append((int(i[0:2]) - 2, int(i[3]) - 1))
                    figure_stay_go.append((int(i[0:2]) + 2, int(i[3]) - 1))
                    figure_stay_go.append((int(i[0:2]) + 2, int(i[3]) + 1))
                elif (i[1] != ' ') and (i[4] in '0123456789'):
                    f_f.append((int(i[0:2]), int(i[3:5])))
                    f_f.append((int(i[0:2]), int(i[3:5]) - 1))
                    f_f.append((int(i[0:2]), int(i[3:5]) + 1))
                    f_f.append((int(i[0:2]) - 2, int(i[3:5]) + 1))
                    f_f.append((int(i[0:2]) - 2, int(i[3:5]) - 1))
                    f_f.append((int(i[0:2]) + 2, int(i[3:5]) - 1))
                    f_f.append((int(i[0:2]) + 2, int(i[3:5]) + 1))

                    figure_stay.append((int(i[0:2]), int(i[3:5])))
                    figure_stay_go.append((int(i[0:2]), int(i[3:5]) - 1))
                    figure_stay_go.append((int(i[0:2]), int(i[3:5]) + 1))
                    figure_stay_go.append((int(i[0:2]) - 2, int(i[3:5]) + 1))
                    figure_stay_go.append((int(i[0:2]) - 2, int(i[3:5]) - 1))
                    figure_stay_go.append((int(i[0:2]) + 2, int(i[3:5]) - 1))
                    figure_stay_go.append((int(i[0:2]) + 2, int(i[3:5]) + 1))

        all_field_boxes = [(y, x) for y in range(N) for x in range(N)]

        free_field_boxes = [(i[1], i[0]) for i in (set(all_field_boxes) - set(f_f))]

        self.table = QTableWidget(N, N)

        self.label = QLabel("No solutions!")

        button = QPushButton("exit")
        button.clicked.connect(self.on_button_cl)

        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)

        with open('output.txt', 'w') as file_1:
            all_varients = []
            one_varient = []
            all_combinations = itertools.combinations(free_field_boxes, L)
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
                        one_varient.append((set(i) - set(z)))
                        if len(list(set(i) - set(z))) == L:
                            for p in figure_stay:
                                file_1.write(str(p) + ' ')
                            for p1 in list(set(i) - set(z)):
                                file_1.write(str(p1[::-1]) + ' ')
                            file_1.write('\n')
                        break
            else:
                file_1.write("No solutions!")

        with open('output.txt', 'r') as file_3:
            f3 = file_3.readlines()
            if 'No solutions!' in f3:
                self.vBox.addWidget(self.label)
                self.vBox.addWidget(button)
            else:
                self.vBox.addWidget(self.table)
                self.vBox.addWidget(button)
                W = []
                W1 = []
                W2 = []
                W2_2 = []
                for i in figure_stay:
                    W2.append((i[1], i[0]))
                    W2_2.append((int(i[1]) - 1, int(i[0])))
                    W2_2.append((int(i[1]) + 1, int(i[0])))
                    W2_2.append((int(i[1]) + 1, int(i[0]) - 2))
                    W2_2.append((int(i[1]) - 1, int(i[0]) - 2))
                    W2_2.append((int(i[1]) - 1, int(i[0]) + 2))
                    W2_2.append((int(i[1]) + 1, int(i[0]) + 2))
                for j in one_varient[0]:
                    W1.append((j[0], j[1]))
                    W.append((int(j[0]) - 1, int(j[1])))
                    W.append((int(j[0]) + 1, int(j[1])))
                    W.append((int(j[0]) + 1, int(j[1]) - 2))
                    W.append((int(j[0]) - 1, int(j[1]) - 2))
                    W.append((int(j[0]) - 1, int(j[1]) + 2))
                    W.append((int(j[0]) + 1, int(j[1]) + 2))
                for i in range(0, N):
                    self.table.setColumnWidth(i, 2)
                    self.table.setRowHeight(i, 2)
                    # self.table.setRowCount(7)
                    # self.table.setColumnCount(7)
                for i in range(0, N):
                    for j in range(0, N):
                        if ((j, i) in W1):
                            self.table.setItem(i, j, QTableWidgetItem("#"))
                        elif ((j, i) in W):
                            self.table.setItem(i, j, QTableWidgetItem("*"))
                        elif ((j, i) in W2):
                            self.table.setItem(i, j, QTableWidgetItem("$"))
                        elif ((j, i) in W2_2):
                            self.table.setItem(i, j, QTableWidgetItem("^"))
                        else:
                            self.table.setItem(i, j, QTableWidgetItem("0"))

    def on_button_cl(self):
        ''' Функция создания кнопки закрытия окна'''
        Window.deleteLater(self)

class MainWindow(QMainWindow):
    ''' Класс для создания главного окна'''
    def __init__(self):
        ''' Первоначальная функция для декорирования главного окна'''
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(695, 533)

        self.adding = AnotherWindow()

        _list1 = self.adding.lineEdit_list

        self.open_window = []

        self.label = QLabel("Введите значение N: ")
        self.label_1 = QLabel("Введите значение L: ")
        self.label_2 = QLabel("Введите значение K: ")

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите размер поля")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setPlaceholderText("Введите количество фигур, которые нужно поставить")
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setPlaceholderText("Введите количество уже поставленных фигур")

        self.button = QPushButton("koordinats")
        self.button_1 = QPushButton("field")
        self.button_2 = QPushButton("exit")

        self.button.clicked.connect(self.get)
        self.button_1.clicked.connect(self.get)
        self.button.clicked.connect(self.on_button_clicked)
        self.button_1.clicked.connect(self.on_button_clicked_1)
        self.button_2.clicked.connect(self.on_button_clicked_2)

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.line_edit, 0, 1)
        layout.addWidget(self.button, 0, 2)

        layout.addWidget(self.label_1, 1, 0)
        layout.addWidget(self.line_edit_1, 1, 1)
        layout.addWidget(self.button_1, 1, 2)

        layout.addWidget(self.label_2, 2, 0)
        layout.addWidget(self.line_edit_2, 2, 1)
        layout.addWidget(self.button_2, 2, 2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    with open('output.txt', 'w') as file3:
        file3.write(f'{0} {0} {0}')

    def get(self, _list1: list):
        ''' Функция для записи данных N L K в файл'''
        text = self.line_edit.text()
        text_1 = self.line_edit_1.text()
        text_2 = self.line_edit_2.text()
        with open('output.txt', 'w') as file:
            file.write(f'{text} {text_1} {text_2}\n')
        with open('output.txt', 'r') as file:
            f = file.readlines()
            if int(f[0][-2]) == 0:
                with open('input.txt', 'w') as file:
                    file.write(f'{text} {text_1} {text_2}\n')

    def on_button_clicked(self):
        ''' Функция для открытия окна для ввода координат фигур'''
        with open('output.txt', 'r') as file_6:
            f6 = file_6.readlines()
        if (len(self.line_edit.text()) > 0) and (len(self.line_edit_1.text()) > 0) and (len(self.line_edit_2.text()) > 0) and (int(f6[0][-2]) != 0):
            new_window = AnotherWindow()
            new_window.show()
            self.open_window.append(new_window)
        else:
            None

    def on_button_clicked_1(self):
        ''' Функция для вывода шахматной доски'''
        with open('input.txt', 'r') as file_6:
            f6 = file_6.readlines()
        if (len(self.line_edit.text()) < 0) and (len(self.line_edit_1.text()) < 0) and (len(self.line_edit_2.text()) < 0) and (len(f6) > 1):
            new_window = Window()
            new_window.show()
            self.open_window.append(new_window)
        if (len(self.line_edit_1.text()) > 0) and (len(f6) > 1):
            new_window = Window()
            new_window.show()
            self.open_window.append(new_window)
        if (len(f6) == 1) and (int(f6[0][-2]) == 0):
            new_window = Window()
            new_window.show()
            self.open_window.append(new_window)
        else:
            None
    def on_button_clicked_2(self):
        ''' Функция для кнопки закрытия окна'''
        MainWindow.deleteLater(self)

if __name__ == '__main__':
    ''' Условие, которое приводит в действие приложение, приводит в действие главное окно'''
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())