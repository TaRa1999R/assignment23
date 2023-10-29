
import sys
import random
from PySide6.QtWidgets import *
from Sudoku_design import Ui_MainWindow

class Mainwindow ( QMainWindow ) :
    
    def __init__ ( self ) :
        super().__init__ ()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self)

        for i in range (9) :
            for j in range (9) :
                new_cell = QLineEdit ()
                self.ui.grid.addWidget ( new_cell , i , j)

if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()