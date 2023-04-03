import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QDialog, QMainWindow
import random

from Ui_main_menu import Ui_main_menu
from Ui_choose_menu import Ui_choose_menu
from Ui_player_menu import Ui_player_menu
from Ui_ai_menu import Ui_ai_menu
from Ui_p_game_menu import Ui_p_game_menu
from Ui_win_menu import Ui_win_menu
from Ui_history_menu import Ui_history_menu


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

    def go_to_p_game_menu(self):            # Lazy fix idrc at this point
        global player1_name
        player1_name = self.player_menu_player1_lineedit.text()
        global player2_name
        player2_name = self.player_menu_player2_lineedit.text()

        widget.addWidget(p_game_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_choose_menu(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

class p_game_menu(QMainWindow, Ui_p_game_menu):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.p1_turn = True
        self.round_value = 0
        self.p1_round_carryover_points = 0
        self.p2_round_carryover_points = 0

        self.setupUi(self)
        self.assign_labels()
        self.connect_signals_slots()

    def assign_labels(self):
        self.p_game_menu_player1_name.setText(player1_name)
        self.p_game_menu_player2_name.setText(player2_name)
        self.p_game_menu_turn_label.setText(str(player1_name)+"'s Turn")

    def connect_signals_slots(self):
        self.p_game_menu_player1_history.clicked.connect(self.go_to_p1_rollhistory)
        self.p_game_menu_player2_history.clicked.connect(self.go_to_p2_rollhistory)
        self.p_game_menu_roll.clicked.connect(self.roll_dice)
        self.p_game_menu_endturn.clicked.connect(self.end_turn)
        self.p_game_menu_exit.clicked.connect(self.go_to_choose_window)

    def go_to_p1_rollhistory(self):
        global game_state
        game_state = "pvp"
        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_p2_rollhistory(self):
        global game_state
        game_state = "pvp"
        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def roll_dice(self):
        dice_value = random.randint(1,6)
        self.p_game_menu_currentdice.setText("You rolled: " + str(dice_value))
        self.round_value = self.round_value + dice_value

        if self.p1_turn == True:
            old_dice_value = self.p1_round_carryover_points
            if dice_value == 6:
                self.round_value = 0
                self.p_game_menu_player1_score.setText(str(old_dice_value))
                self.end_turn()
            self.p_game_menu_player1_score.setText(str(self.round_value + old_dice_value))

            if self.round_value + old_dice_value >= 40:
                pass

        else:
            old_dice_value = self.p2_round_carryover_points
            if dice_value == 6:
                self.round_value = 0
                self.p_game_menu_player2_score.setText(str(old_dice_value))
                self.end_turn()
            self.p_game_menu_player2_score.setText(str(self.round_value + old_dice_value))

    def end_turn(self):
        self.round_value = 0

        if self.p1_turn:
            self.p_game_menu_turn_label.setText(str(player2_name)+"'s Turn")
            self.p1_round_carryover_points = int(self.p_game_menu_player1_score.text())
            self.p1_turn = False
        else:
            self.p_game_menu_turn_label.setText(str(player1_name)+"'s Turn")
            self.p2_round_carryover_points = int(self.p_game_menu_player2_score.text())
            self.p1_turn = True

    def go_to_choose_window(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_win_menu(self):
        pass

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

class win_menu(QMainWindow, Ui_win_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        pass

class history_menu(QMainWindow, Ui_history_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.history_menu_back.clicked.connect(self.go_to_game_menu)

    def go_to_game_menu(self):
        if game_state == "pvp":
            widget.addWidget(p_game_menu())
            widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    mainwindow=main_window()
    widget.addWidget(mainwindow)
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec())