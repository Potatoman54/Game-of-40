import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QDialog, QMainWindow
import random
import time

from Ui_main_menu import Ui_main_menu
from Ui_choose_menu import Ui_choose_menu
from Ui_player_menu import Ui_player_menu
from Ui_ai_menu import Ui_ai_menu
from Ui_p_game_menu import Ui_p_game_menu
from Ui_win_menu import Ui_win_menu
from Ui_history_menu import Ui_history_menu
from Ui_a_game_menu import Ui_a_game_menu


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
        global ai_name
        ai_name = self.choose_menu_ai_choose.currentText()
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
        global p1_turn
        p1_turn = True
        global round_value
        round_value = 0
        global p1_round_carryover_points
        p1_round_carryover_points = 0
        global p2_round_carryover_points
        p2_round_carryover_points = 0
        global p1_wins
        p1_wins = 0
        global p2_wins
        p2_wins = 0
        global p1_dice_rolls
        p1_dice_rolls = []
        global p2_dice_rolls
        p2_dice_rolls = []

        widget.addWidget(p_game_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        global player_name
        player_name = self.ai_menu_player_lineedit.text()
        global player_turn
        player_turn = True
        global a_round_value
        a_round_value = 0
        global player_round_carryover_points
        player_round_carryover_points = 0
        global ai_round_carryover_points
        ai_round_carryover_points = 0
        global player_wins
        player_wins = 0
        global ai_wins
        ai_wins = 0
        global player_dice_rolls
        player_dice_rolls = []
        global ai_dice_rolls
        ai_dice_rolls = []

        widget.addWidget(a_game_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_choose_menu(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

class p_game_menu(QMainWindow, Ui_p_game_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.assign_labels()
        self.connect_signals_slots()

    def assign_labels(self):
        self.p_game_menu_player1_name.setText(player1_name)
        self.p_game_menu_player2_name.setText(player2_name)
        global p1_turn
        if p1_turn:
            self.p_game_menu_turn_label.setText(str(player1_name)+"'s Turn")
        else:
            self.p_game_menu_turn_label.setText(str(player2_name)+"'s Turn")
        self.p_game_menu_player1_score.setText(str(p1_round_carryover_points + round_value))
        self.p_game_menu_player2_score.setText(str(p2_round_carryover_points + round_value))
        self.p_game_menu_player1_wins.setText(str(p1_wins))
        self.p_game_menu_player2_wins.setText(str(p2_wins))

    def connect_signals_slots(self):
        self.p_game_menu_player1_history.clicked.connect(self.go_to_p1_rollhistory)
        self.p_game_menu_player2_history.clicked.connect(self.go_to_p2_rollhistory)
        self.p_game_menu_roll.clicked.connect(self.roll_dice)
        self.p_game_menu_endturn.clicked.connect(self.end_turn)
        self.p_game_menu_exit.clicked.connect(self.go_to_choose_window)

    def go_to_p1_rollhistory(self):
        global game_state
        game_state = "pvp"

        global history_viewer
        history_viewer = "p1"

        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_p2_rollhistory(self):
        global game_state
        game_state = "pvp"

        global history_viewer
        history_viewer = "p2"

        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def roll_dice(self):
        global round_value
        dice_value = random.randint(1,6)
        self.p_game_menu_currentdice.setText("You rolled: " + str(dice_value))
        round_value = round_value + dice_value

        global p1_turn
        global p1_round_carryover_points
        global p2_round_carryover_points
        global p2_dice_rolls
        if p1_turn == True:
            global p1_dice_rolls
            p1_dice_rolls.append(dice_value)
            old_dice_value = p1_round_carryover_points

            if dice_value == 6:
                round_value = 0
                self.p_game_menu_player1_score.setText(str(old_dice_value))
                self.end_turn()

            self.p_game_menu_player1_score.setText(str(round_value + old_dice_value))

            if round_value + old_dice_value >= 40:
                self.go_to_win_menu("p1")
                global p1_wins
                p1_wins = p1_wins + 1

                round_value = 0
                p1_turn = True
                p1_round_carryover_points = 0
                p2_round_carryover_points = 0
                p1_dice_rolls = []
                p2_dice_rolls = []

        else:  
            p2_dice_rolls.append(dice_value)
            old_dice_value = p2_round_carryover_points
            if dice_value == 6:
                round_value = 0
                self.p_game_menu_player2_score.setText(str(old_dice_value))
                self.end_turn()
            self.p_game_menu_player2_score.setText(str(round_value + old_dice_value))

            if round_value + old_dice_value >= 40:
                self.go_to_win_menu("p2")
                global p2_wins
                p2_wins = p2_wins + 1

                round_value = 0
                p1_turn = True
                p1_round_carryover_points = 0
                p2_round_carryover_points = 0
                p1_dice_rolls = []
                p2_dice_rolls = []

    def end_turn(self):
        global p1_round_carryover_points
        global p2_round_carryover_points
        global round_value
        round_value = 0
        global p1_turn

        if p1_turn:
            self.p_game_menu_turn_label.setText(str(player2_name)+"'s Turn")
            p1_round_carryover_points = int(self.p_game_menu_player1_score.text())
            p1_turn = False
        else:
            self.p_game_menu_turn_label.setText(str(player1_name)+"'s Turn")
            p2_round_carryover_points = int(self.p_game_menu_player2_score.text())
            p1_turn = True

    def go_to_choose_window(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_win_menu(self, win):
        global game_state
        game_state = "pvp"

        global winner
        winner = win

        widget.addWidget(win_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)    

class a_game_menu(QMainWindow, Ui_a_game_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.assign_labels()
        self.connect_signals_slots()

    def assign_labels(self):
        self.a_game_menu_player_name.setText(player_name)
        self.a_game_menu_ai_name.setText(ai_name)
        global player_turn
        if player_turn:
            self.a_game_menu_turn_label.setText(str(player_name)+"'s Turn")
        else:
            self.a_game_menu_turn_label.setText(str(ai_name)+"'s Turn")
        self.a_game_menu_player_dicescore.setText(str(player_round_carryover_points + a_round_value))
        self.a_game_menu_ai_dicescore.setText(str(ai_round_carryover_points + a_round_value))
        self.a_game_menu_player_score.setText(str(player_wins))
        self.a_game_menu_ai_score.setText(str(ai_wins))

    def connect_signals_slots(self):
        self.a_game_menu_player_rollhistory.clicked.connect(self.go_to_player_rollhistory)
        self.a_game_menu_ai_rollhistory.clicked.connect(self.go_to_ai_rollhistory)
        self.a_game_menu_roll.clicked.connect(self.roll_dice)
        self.a_game_menu_endturn.clicked.connect(self.end_turn)
        self.a_game_menu_end.clicked.connect(self.go_to_choose_window)

    def go_to_player_rollhistory(self):
        global game_state
        game_state = "ai"

        global history_viewer
        history_viewer = "player"

        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_ai_rollhistory(self):
        global game_state
        game_state = "ai"

        global history_viewer
        history_viewer = "ai"

        widget.addWidget(history_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def roll_dice(self):
        global a_round_value
        dice_value = random.randint(1,6)
        self.a_game_menu_dicescore.setText("You rolled: " + str(dice_value))
        a_round_value = a_round_value + dice_value

        global player_turn
        global player_round_carryover_points
        global ai_round_carryover_points
        global ai_dice_rolls

        if player_turn == True:
            global player_dice_rolls
            player_dice_rolls.append(dice_value)
            old_dice_value = player_round_carryover_points

            if dice_value == 6:
                a_round_value = 0
                self.a_game_menu_player_dicescore.setText(str(old_dice_value))
                self.end_turn()

            self.a_game_menu_player_dicescore.setText(str(a_round_value + old_dice_value))

            if a_round_value + old_dice_value >= 40:
                self.go_to_win_menu("player")
                global player_wins
                player_wins = player_wins + 1

                a_round_value = 0
                player_turn = True
                player_round_carryover_points = 0
                ai_round_carryover_points = 0
                player_dice_rolls = []
                ai_dice_rolls = []

    def end_turn(self):
        global player_round_carryover_points
        global ai_round_carryover_points
        global a_round_value
        a_round_value = 0
        global player_turn
        global ai_name

        if player_turn:
            self.a_game_menu_turn_label.setText(str(ai_name)+"'s Turn")
            player_round_carryover_points = int(self.a_game_menu_player_dicescore.text())
            player_turn = False
            self.ai_turn()
        else:
            self.a_game_menu_turn_label.setText(str(player_name)+"'s Turn")
            ai_round_carryover_points = int(self.a_game_menu_ai_dicescore.text())
            player_turn = True
            self.a_game_menu_roll.setEnabled(True)
            self.a_game_menu_endturn.setEnabled(True)

    def ai_turn(self):
        global ai_round_carryover_points
        global a_round_value
        global ai_dice_rolls
        global ai_name
        global player_turn
        global player_round_carryover_points
        global ai_round_carryover_points
        global ai_dice_rolls
        global player_dice_rolls
        global player_wins
        global ai_wins

        self.a_game_menu_roll.setEnabled(False)
        self.a_game_menu_endturn.setEnabled(False)

        if ai_name == "Medium":
            dice_value1 = random.randint(1,6)
            time.sleep(0.5)
            self.a_game_menu_dicescore.setText("You rolled: " + str(dice_value1))
            a_round_value = a_round_value + dice_value1
            old_dice_value = ai_round_carryover_points
            if dice_value1 != 6:
                ai_dice_rolls.append(dice_value1)
                self.a_game_menu_ai_dicescore.setText(str(a_round_value + old_dice_value))

                if a_round_value + old_dice_value >= 40:
                    self.go_to_win_menu("ai")
                    
                    ai_wins = ai_wins + 1

                    a_round_value = 0
                    player_turn = True
                    player_round_carryover_points = 0
                    ai_round_carryover_points = 0
                    player_dice_rolls = []
                    ai_dice_rolls = []

                
                
                
                self.end_turn()

                
            else:
                a_round_value = 0
                self.a_game_menu_ai_dicescore.setText(str(old_dice_value))
                self.end_turn()

        else:
            print("Hard")
        
    def go_to_choose_window(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_win_menu(self, win):
        global game_state
        game_state = "ai"

        global winner
        winner = win

        widget.addWidget(win_menu())
        widget.setCurrentIndex(widget.currentIndex()+1)

class win_menu(QMainWindow, Ui_win_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.assignwinner()
        self.connect_signals_slots()

    def assignwinner(self):
        global player1_name
        global player2_name
        global player_name
        global ai_name

        if winner == "p1":
            self.win_menu_label.setText(player1_name + " Wins!")
        elif winner == "p2":
            self.win_menu_label.setText(player2_name + " Wins!")
        elif winner == "player":
            self.win_menu_label.setText(player_name + " Wins!")
        else:
            self.win_menu_label.setText(ai_name + " Wins!")

    def connect_signals_slots(self):
        self.win_menu_continue.clicked.connect(self.go_to_game_menu)
        self.win_menu_exit.clicked.connect(self.go_to_choose_menu)

    def go_to_game_menu(self):
        if game_state == "pvp":
            widget.addWidget(p_game_menu())
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            widget.addWidget(a_game_menu())
            widget.setCurrentIndex(widget.currentIndex()+1)

    def go_to_choose_menu(self):
        widget.addWidget(choose_window())
        widget.setCurrentIndex(widget.currentIndex()+1)

class history_menu(QMainWindow, Ui_history_menu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.assign_label()
        self.connect_signals_slots()

    def assign_label(self):
        global game_state
        global history_viewer

        if game_state == "pvp":
            if history_viewer == "p1":
                p1_dice_rolls_label = QLabel(text="Rolls by " + player1_name + " during this round: " + str(p1_dice_rolls))
                self.history_menu_scrollarea.setWidget(p1_dice_rolls_label)
            else:
                p2_dice_rolls_label = QLabel(text="Rolls by " + player2_name + " during this round: " + str(p2_dice_rolls))
                self.history_menu_scrollarea.setWidget(p2_dice_rolls_label)
        else:
            if history_viewer == "player":
                player_dice_rolls_label = QLabel(text="Rolls by " + player_name + " during this round: " + str(player_dice_rolls))
                self.history_menu_scrollarea.setWidget(player_dice_rolls_label)
            else:
                ai_dice_rolls_label = QLabel(text="Rolls by " + ai_name + " during this round: " + str(ai_dice_rolls))
                self.history_menu_scrollarea.setWidget(ai_dice_rolls_label)

    def connect_signals_slots(self):
        self.history_menu_back.clicked.connect(self.go_to_game_menu)

    def go_to_game_menu(self):
        if game_state == "pvp":
            widget.addWidget(p_game_menu())
            widget.setCurrentIndex(widget.currentIndex()+1)

        else:
            widget.addWidget(a_game_menu())
            widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    mainwindow=main_window()
    widget.addWidget(mainwindow)
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec())