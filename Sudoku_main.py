
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
        puzzle = Sudoku (3).difficulty (0.5)
        self.cells = [[None for i in range (9)] for j in range (9)]

        for i in range (9) :
            for j in range (9) :
                new_cell = QLineEdit ()
                new_cell.setSizePolicy (QSizePolicy.Maximum , QSizePolicy.MinimumExpanding)
                new_cell.setStyleSheet ("background-color: rgb(0,255,255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                new_cell.setAlignment (Qt.AlignHCenter)
                new_cell.setFont (QFont ("Segoe UI" , 13))
                if puzzle.board[i][j] != None :
                    new_cell.setText (str (puzzle.board[i][j]))
                    new_cell.setReadOnly (True)

                self.ui.grid.addWidget ( new_cell , i , j)
                self.cells[i][j] = new_cell
                new_cell.textChanged.connect (partial (self.validation , i , j) )

    def validation ( self , i , j , text) : 
        if text not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"] :
            self.cells[i][j].setText ("")


    def check ( self ) : ...

if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()