
import sys
import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from sudoku import Sudoku
from Sudoku_design import Ui_MainWindow

class Mainwindow ( QMainWindow ) :
    
    def __init__ ( self ) :
        super().__init__ ()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

        for i in range (9) :
            for j in range (9) :
                new_cell = QLineEdit ()
                new_cell.setSizePolicy (QSizePolicy.MinimumExpanding , QSizePolicy.MinimumExpanding)
                new_cell.setStyleSheet ("background-color: rgb(0,255,255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                new_cell.setAlignment (Qt.AlignHCenter)
                new_cell.setFont (QFont ("Segoe UI" , 13))
                self.ui.grid.addWidget ( new_cell , i , j)

if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()