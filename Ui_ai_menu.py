# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jakub\Visual Studio Code\Game of 40\ai_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ai_menu(object):
    def setupUi(self, ai_menu):
        ai_menu.setObjectName("ai_menu")
        ai_menu.resize(400, 300)
        self.ai_menu_label = QtWidgets.QLabel(ai_menu)
        self.ai_menu_label.setGeometry(QtCore.QRect(70, 20, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(26)
        self.ai_menu_label.setFont(font)
        self.ai_menu_label.setObjectName("ai_menu_label")
        self.ai_menu_player_label = QtWidgets.QLabel(ai_menu)
        self.ai_menu_player_label.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.ai_menu_player_label.setObjectName("ai_menu_player_label")
        self.ai_menu_player_lineedit = QtWidgets.QLineEdit(ai_menu)
        self.ai_menu_player_lineedit.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.ai_menu_player_lineedit.setObjectName("ai_menu_player_lineedit")
        self.ai_menu_start = QtWidgets.QPushButton(ai_menu)
        self.ai_menu_start.setGeometry(QtCore.QRect(40, 250, 75, 23))
        self.ai_menu_start.setObjectName("ai_menu_start")
        self.ai_menu_back = QtWidgets.QPushButton(ai_menu)
        self.ai_menu_back.setGeometry(QtCore.QRect(270, 250, 75, 23))
        self.ai_menu_back.setObjectName("ai_menu_back")

        self.retranslateUi(ai_menu)
        QtCore.QMetaObject.connectSlotsByName(ai_menu)

    def retranslateUi(self, ai_menu):
        _translate = QtCore.QCoreApplication.translate
        ai_menu.setWindowTitle(_translate("ai_menu", "Dialog"))
        self.ai_menu_label.setText(_translate("ai_menu", "Choose your name"))
        self.ai_menu_player_label.setText(_translate("ai_menu", "Player name"))
        self.ai_menu_start.setText(_translate("ai_menu", "Start"))
        self.ai_menu_back.setText(_translate("ai_menu", "Back"))
