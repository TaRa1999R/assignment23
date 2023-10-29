
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
        self.cells = [[None for i in range (9)] for j in range (9)]
        
        self.new_game ()
        self.ui.menue_new.triggered.connect (self.new_game)
        self.ui.menue_file.triggered.connect (self.open_file)
        self.ui.menue_rule.triggered.connect (self.rules)
        self.ui.menue_option.triggered.connect (self.options)
    
    
    def new_game ( self ) :
        puzzle = Sudoku (3 , seed = random.randint (1 , 1000)).difficulty (0.5)
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

    
    def open_file ( self ) :
        path = QFileDialog.getOpenFileName (self , "Open File")[0]
        f = open (path , "r")
        big_text = f.read ()
        rows = big_text.split ("\n")
        puzzle = [[ None for i in range (9)] for j in range (9)]
        for i in range (len (rows)) :
            cell = rows[i].split (" ")
            for j in range (len (cell)) :
                puzzle[i][j] = int (cell[j])

        for i in range (9) :
            for j in range (9) :
                self.cells[i][j].setReadOnly (False)
                if puzzle[i][j] != 0 :
                    self.cells[i][j].setText (str (puzzle[i][j]))
                    self.cells[i][j].setReadOnly (True)
                
                else :
                    self.cells[i][j].setText ("")


    def rules ( self ) :
        text = "What are the 3 rules of Sudoku?🤔\n\nThe rules for sudoku are simple :\n\
    1. Each 3×3 block can only contain numbers from 1 to 9.\n    2.Each vertical column can only contain numbers from 1 to 9.\n\
    3.Each horizontal row can only contain numbers from 1 to 9.\n\n\
tip :Each number in the 3×3 block, vertical column or horizontal row can be used only once🤐😅\n\n I hope you enjoy my game"
        message = QMessageBox (windowTitle = "Sudoku Ruls 📜" , text = text)
        message.exec_ ()


    def options ( self ) : 
        text = "✔ You can change the difficulty of the game.\n\n✔ You can solve your own Sudoku by writing its numbers in a text file a use \
'Open File' section in 'Game' menue.\nnote : You must write '0' instead of empty blocks😉"
        message = QMessageBox (windowTitle = "Options ..." , text = text)
        message.exec_ ()


    def validation ( self , i , j , text) : 
        if text not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"] :
            self.cells[i][j].setText ("")
        
        else :
            self.check ()


    def check ( self ) : ...

if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()