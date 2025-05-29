import itertools
import sys
import ast
from Chess import *
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QRegularExpressionValidator, QColor, QPainter, QBrush
from PySide6.QtWidgets import QLineEdit, QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow, QGridLayout

class Wrong_koordinates(QWidget):
    ''' Класс для создания окна при вводе неправильных координат фигур'''
    def __init__(self):
        ''' Начальная функция для декорирования окна'''
        super().__init__()
        self.setWindowTitle("Error")
        self.resize(100, 100)
        self.layout = QVBoxLayout()

        self.label = QLabel("Были введены координаты под ударом. Координаты не будут записаны в файл.")

        self.button = QPushButton("Exit")
        self.button.clicked.connect(self.on_button_cl)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def on_button_cl(self):
        ''' Функция для кнопки закрытия'''
        Wrong_koordinates.deleteLater(self)

class FieldWindow(QWidget):
    ''' Класс для создания окна с доской'''
    def __init__(self):
        ''' Функция для декорирования окна'''
        super().__init__()
        self.setWindowTitle("Field")
        self.resize(695, 533)

        self.show()

        self.vBox = QVBoxLayout()
        self.setLayout(self.vBox)
        with open('input.txt', 'r') as file_3:
            with open('output.txt', 'r') as file_4:
                f1 = file_4.readlines()
                f = file_3.readlines()
                k = ''
                for i in f[0]:
                    while i != ' ':
                        k += str(i)
                        break

                if 'No solutions!' in f1:
                    self.label = QLabel("No solutions!")
                    self.button = QPushButton("exit")
                    self.button.clicked.connect(self.on_button_click)
                    self.vBox.addWidget(self.label)
                    self.vBox.addWidget(self.button)
                else:
                    self.scene = QGraphicsScene()
                    self.view = QGraphicsView()
                    self.view.setScene(self.scene)
                    self.view.setRenderHint(QPainter.Antialiasing)
                    self.vBox.addWidget(self.view)
                    self.setScene(self.scene)

                    self.view.setBackgroundBrush(QBrush(QColor("#FFFFFF")))
                    self.view.setSceneRect(0, 0, int(k) / 5 + 6, int(k) / 5 - 2)
                    self.scene.setSceneRect(self.view.sceneRect())

                    for i in range(int(k)):
                        for j in range(int(k)):
                            if (j, i) in Chess.W:
                                rect_item = QGraphicsRectItem(j*20, i*20, 20, 20)
                                rect_item.setBrush(Qt.red)
                                self.scene.addItem(rect_item)
                            elif (j, i) in Chess.W2:
                                rect_item = QGraphicsRectItem(j * 20, i * 20, 20, 20)
                                rect_item.setBrush(Qt.yellow)
                                self.scene.addItem(rect_item)
                            elif (j, i) in Chess.W1:
                                rect_item = QGraphicsRectItem(j * 20, i * 20, 20, 20)
                                rect_item.setBrush(Qt.blue)
                                self.scene.addItem(rect_item)
                            else:
                                rect_item = QGraphicsRectItem(j * 20, i * 20, 20, 20)
                                rect_item.setBrush(Qt.white)
                                self.scene.addItem(rect_item)

                    self.button = QPushButton("exit")
                    self.button.clicked.connect(self.on_button_click)
                    self.view.setFixedSize(self.view.sizeHint())
                    self.vBox.addWidget(self.view)
                    self.vBox.addWidget(self.button)

    def on_button_click(self):
        ''' Функция для кнопки закрытия окна'''
        FieldWindow.deleteLater(self)

    def setScene(self, scene):
        ''' Функция для работы setScene'''
        pass

class AnotherWindow(QWidget):
    ''' Класс для создания окна с ввода координат'''
    def __init__(self):
        ''' Фунуия для декорирования окна'''
        super().__init__()
        self.setWindowTitle("Adding window")
        self.resize(695, 533)
        self.widget = QWidget()
        self.layout = QGridLayout(self.widget)

        self.open_window = []

        self.label = QLabel()
        self.button = QPushButton("enter")
        self.button_1 = QPushButton("exit")
        self.button.clicked.connect(Chess.koordinats_giving)
        self.button_1.clicked.connect(self.on_button_click)

        with open('output.txt', 'r') as file:
            f = file.readline()
            N, L, K = map(int, f.strip().split())
        if K > 1:
            count_K = 0
            for i in range(1, K):
                for j in range(0, K):
                    while count_K < K:
                        self.line_edit = QLineEdit()
                        Chess.lineEdit_list.append(self.line_edit)
                        self.layout.addWidget(self.line_edit, i, j)
                        count_K += 1
                        break
        else:
            self.line_edit = QLineEdit()
            Chess.lineEdit_list.append(self.line_edit)
            self.layout.addWidget(self.line_edit, 0, 0)

        self.layout1 = QVBoxLayout()
        self.layout1.addWidget(self.label)
        self.layout1.addWidget(self.widget)
        self.layout1.addWidget(self.button)
        self.layout1.addWidget(self.button_1)
        self.setLayout(self.layout1)

    def on_button_click(self):
        ''' Функция для кнопки закрытия окна'''
        AnotherWindow.deleteLater(self)

class MainWindow(QMainWindow):
    ''' Класс для создания главного окна'''
    def __init__(self):
        ''' Функция для декорирования главного окна'''
        super().__init__()
        self.setWindowTitle("Main Window")
        self.resize(695, 533)

        self.open_window = []

        self.label = QLabel("Введите значение N: ")
        self.label_1 = QLabel("Введите значение L: ")
        self.label_2 = QLabel("Введите значение K: ")

        self.validator = QRegularExpressionValidator(QRegularExpression("^[0-9]+$"))
        self.line_edit = QLineEdit()
        self.line_edit.setValidator(self.validator)
        self.line_edit.setPlaceholderText("Введите размер поля")
        self.line_edit_1 = QLineEdit()
        self.line_edit_1.setValidator(self.validator)
        self.line_edit_1.setPlaceholderText("Введите количество фигур, которые нужно поставить")
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setValidator(self.validator)
        self.line_edit_2.setPlaceholderText("Введите количество уже поставленных фигур")

        self.button = QPushButton("koordinats")
        self.button_1 = QPushButton("field")
        self.button_2 = QPushButton("exit")

        self.button.clicked.connect(self.good_bad_koordinats)
        self.button.clicked.connect(Chess.good_bad_koordinats)
        self.button_1.clicked.connect(Chess.solutions)
        self.button_1.clicked.connect(Chess.table_koord)
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

    def on_button_clicked(self):
        ''' Функция для кнопки для запуска окна ввода координат'''
        with open('input.txt', 'r') as file_6:
            f6 = file_6.readlines()
            if (len(self.line_edit.text()) > 0) and (len(self.line_edit_1.text()) > 0) and (len(self.line_edit_2.text()) > 0) and (int(f6[0][0]) != 0):
                new_window = AnotherWindow()
                new_window.show()
                self.open_window.append(new_window)
            else:
                None
    def on_button_clicked_1(self):
        ''' Функция для кнопки вывода доски'''
        with open('input.txt', 'r') as file_6:
            f6 = file_6.readlines()
        if (len(self.line_edit.text()) < 0) and (len(self.line_edit_1.text()) < 0) and (len(self.line_edit_2.text()) < 0) and (len(f6) > 1):
            new_window = FieldWindow()
            new_window.show()
            self.open_window.append(new_window)
        if (len(self.line_edit_1.text()) > 0) and (len(f6) > 1):
            new_window = FieldWindow()
            new_window.show()
            self.open_window.append(new_window)
        if f6[0][0] != ' ':
            if (len(f6) == 1) and (int(f6[0][-2]) == 0):
                new_window = FieldWindow()
                new_window.show()
                self.open_window.append(new_window)
        else:
            None

    def good_bad_koordinats(self):
        ''' Функция для записи данных в файл с главного окна'''
        text = self.line_edit.text()
        text_1 = self.line_edit_1.text()
        text_2 = self.line_edit_2.text()
        with open('input.txt', 'w') as file:
            file.write(f'{text} {text_1} {text_2}\n')

    def on_button_clicked_2(self):
        ''' Функция для кнопки закрытия окна'''
        MainWindow.deleteLater(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())