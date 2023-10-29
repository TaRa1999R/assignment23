# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sudoku.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 610)
        MainWindow.setStyleSheet(u"background-color: rgb(129, 129, 129);")
        self.menue_new = QAction(MainWindow)
        self.menue_new.setObjectName(u"menue_new")
        self.menue_file = QAction(MainWindow)
        self.menue_file.setObjectName(u"menue_file")
        self.menue_rule = QAction(MainWindow)
        self.menue_rule.setObjectName(u"menue_rule")
        self.menue_difficulty = QAction(MainWindow)
        self.menue_difficulty.setObjectName(u"menue_difficulty")
        self.menue_option = QAction(MainWindow)
        self.menue_option.setObjectName(u"menue_option")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 85, 127);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")

        self.horizontalLayout.addWidget(self.label)

        self.mistakes = QLineEdit(self.centralwidget)
        self.mistakes.setObjectName(u"mistakes")
        self.mistakes.setFont(font)
        self.mistakes.setStyleSheet(u"color: rgb(255, 85, 127);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")

        self.horizontalLayout.addWidget(self.mistakes)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 255, 127);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")

        self.horizontalLayout.addWidget(self.label_2)

        self.score = QLineEdit(self.centralwidget)
        self.score.setObjectName(u"score")
        self.score.setFont(font)
        self.score.setStyleSheet(u"color: rgb(0, 255, 127);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;")

        self.horizontalLayout.addWidget(self.score)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.grid = QGridLayout()
        self.grid.setObjectName(u"grid")

        self.gridLayout_2.addLayout(self.grid, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 499, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menuGame.addAction(self.menue_new)
        self.menuGame.addAction(self.menue_file)
        self.menuGame.addAction(self.menue_difficulty)
        self.menuabout.addAction(self.menue_rule)
        self.menuabout.addAction(self.menue_option)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SuDoKu", None))
        self.menue_new.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menue_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.menue_rule.setText(QCoreApplication.translate("MainWindow", u"Rules", None))
        self.menue_difficulty.setText(QCoreApplication.translate("MainWindow", u"Difficulty", None))
        self.menue_option.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mistakes :", None))
        self.mistakes.setInputMask("")
        self.mistakes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Score :", None))
        self.score.setInputMask("")
        self.score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

