from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(250,250, 300, 300)
    label = QtWidgets.QLabel(win)
    but = QtWidgets.QPushButton(win)
    but.setText('Tekst')
    but.move(50, 50)
    label.setText('Jakis tekst')
    win.setWindowTitle('Nazwa')
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()