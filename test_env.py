import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QDialog, QMainWindow

from Ui_main_menu import Ui_main_menu
from Ui_choose_menu import Ui_choose_menu
from Ui_player_menu import Ui_player_menu
from Ui_ai_menu import Ui_ai_menu


class main_window(QMainWindow, Ui_main_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.main_menu_exit.clicked.connect(self.shutdown)
        self.main_menu_start.clicked.connect(self.change_window)

    def change_window(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def shutdown(self):
        sys.exit(app.exec_())

class choose_window(QMainWindow, Ui_choose_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.choose_menu_back.clicked.connect(self.go_to_main_menu)
        self.choose_menu_vs_player.clicked.connect(self.go_to_player_menu)
        self.choose_menu_vs_ai.clicked.connect(self.go_to_ai_menu)
    
    def go_to_main_menu(self):
        widget.addWidget(main_window())
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def go_to_player_menu(self):
        widget.addWidget(player_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def go_to_ai_menu(self):
        widget.addWidget(ai_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

class player_menu(QMainWindow, Ui_player_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.player_menu_start.clicked.connect(self.go_to_p_game_menu)
        self.player_menu_back.clicked.connect(self.go_to_choose_menu)

    def go_to_p_game_menu(self):
        pass

    def go_to_choose_menu(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

class ai_menu(QMainWindow, Ui_ai_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.ai_menu_start.clicked.connect(self.go_to_a_game_menu)
        self.ai_menu_back.clicked.connect(self.go_to_choose_menu)

    def go_to_a_game_menu(self):
        pass

    def go_to_choose_menu(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    mainwindow=main_window()
    widget.addWidget(mainwindow)
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec())