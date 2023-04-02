import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from Ui_main_menu import Ui_main_menu
from Ui_choose_menu import Ui_choose_menu

class main_window(QMainWindow, Ui_main_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.main_menu_exit.clicked.connect(self.close)
        self.main_menu_start.clicked.connect(self.change_window)

    def change_window(self):
        self.hide()
        choose_window(self).show()

class choose_window(QMainWindow, Ui_choose_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main_window()
    win.show()
    sys.exit(app.exec())