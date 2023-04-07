<<<<<<< HEAD
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Установка каталитического крекинга')
        self.setGeometry(600, 250, 600, 600)

def application():
    app = QApplication(sys.argv)
    # label = QLabel("Fluid catalytic cracking", alignment=Qt.AlignCenter)
    # label.show()
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
=======
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QLabel,
                             QVBoxLayout)

import sys


class MainWindow(QWidget):
    """Подкласс QMainWindow для настройки главного окна вашего приложения"""

    def __init__(self):
        super().__init__()

        self.label = QLabel("<center>Привет, мир!</center>")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.btn_quit = QPushButton("&Закрыит окно")
        self.setWindowTitle("Первая программа")
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btn_quit)
        self.setLayout(self.vbox)
        self.btn_quit.clicked.connect(quit)
        self.resize(800, 600)


if __name__ == '__main__':
    # Вам нужен один (и только один) экземпляр QApplication для каждого приложения.
    # Передайте sys.argv, чтобы разрешить аргументы командной строки для вашего приложения.
    # Если вы знаете, что не будете использовать аргументы командной строки, QApplication([]) тоже подойдет.
    app = QApplication(sys.argv)

    # Создаем виджет Qt, который будет нашим окном.
    window = MainWindow()
    window.show()  # ВАЖНО!!!!! Окна по умолчанию скрыты.

    # Запустить цикл обработки событий.
    app.exec()

    # Ваше приложение не попадет сюда, пока вы не выйдете и событие
    # цикл остановлен.
>>>>>>> 2124f02eab16c952979d6676a90ad261af4f56f9
