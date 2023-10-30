
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
        self.score = 0
        self.mistake = 0
        self.ui.darkmode.setChecked (True)
    
        
        self.new_game ()
        self.ui.menue_new.triggered.connect (self.new_game)
        self.ui.menue_file.triggered.connect (self.open_file)
        self.ui.menue_rule.triggered.connect (self.rules)
        self.ui.menue_option.triggered.connect (self.options)
        self.ui.darkmode.clicked.connect (self.change_mode)
    
    
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
        try :
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
        
        except :
            txt = "Sorry the an error has been occured.😕\nPlease check option section in about menue and try again later.⏳\n\
Untill then you cant do another sudoku puzzle.😇😕⏳"
            message = QMessageBox (windowTitle = "⚠ Error ..." , text = txt)
            message.exec_ ()
            self.new_game ()


    def rules ( self ) :
        txt = "What are the 3 rules of Sudoku?🤔\n\nThe rules for sudoku are simple :\n\
    1. Each 3*3 block can only contain numbers from 1 to 9.\n    2.Each vertical column can only contain numbers from 1 to 9.\n\
    3.Each horizontal row can only contain numbers from 1 to 9.\n\n\
tip :Each number in the 3*3 block, vertical column or horizontal row can be used only once🤐😅\n\n I hope you enjoy my game"
        message = QMessageBox (windowTitle = "Sudoku Ruls 📜" , text = txt)
        message.exec_ ()


    def options ( self ) : 
        txt = "✔ You can solve your own Sudoku by writing its numbers in a text file a use \
'Open File' section in 'Game' menue.\nnote : You must write '0' instead of empty blocks😉\n\n✔ You can use 'Solve' section in 'Game' menue to \
too see the completed sudoku puzzle.\nnote : You can only use this option for the game puzzle not the one you upload them😏\n\n✔ Default game mode \
is 'Dark Mode' , but you can also turn it off and put the game in 'Light Mode'."
        message = QMessageBox (windowTitle = "Options ..." , text = txt)
        message.exec_ ()

    def change_mode ( self ) :
        if self.ui.darkmode.isChecked () == True :
            self.ui.centralwidget.setStyleSheet("background-color: rgb(129, 129, 129);")
            for i in range (9) :
                for j in range (9) :
                    self.cells[i][j].setStyleSheet("background-color: rgb(0, 255, 255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
        
        else :
            self.ui.centralwidget.setStyleSheet("background-color: rgb(25, 255, 255);")
            for i in range (9) :
                for j in range (9) :
                    self.cells[i][j].setStyleSheet("background-color: rgb(253, 202, 255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")


    def solve ( self ) :
        ...


    def validation ( self , i , j , text) : 
        if text not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"] :
            if self.ui.darkmode.isChecked () == True :
                self.cells[i][j].setStyleSheet ("background-color: rgb(0, 255, 255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                self.cells[i][j].setText ("")
            
            else :
                self.cells[i][j].setStyleSheet ("background-color: rgb(253, 202, 255); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                self.cells[i][j].setText ("") 

        else :    
            self.check (i , j , text)


    def check ( self , i , j , text) :
        state = 0
        # CHECK  IN A ROW
        if state == 0 :
            for colomn in range (9) :
                if colomn != j :
                    if text == self.cells[i][colomn].text() :
                        self.cells[i][j].setStyleSheet ("background-color: rgb(255, 85, 127); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                        self.mistake += 1
                        self.ui.mistakes.setText (str (self.mistake))
                        print("ro", self.mistake)
                        break
                
            else :
                state = 1
        
        # CHECK IN A COLOMN
        if state == 1 :
            for row in range (9) :
                if row != i :
                    if text == self.cells[row][j].text() :
                        self.cells[i][j].setStyleSheet ("background-color: rgb(255, 85, 127); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                        self.mistake += 1
                        self.ui.mistakes.setText (str (self.mistake))
                        print("col", self.mistake)
                        break

            else :
                state = 2

        # CHECK IN 3*3 BLOCK
        if state == 2 :
            if i % 3 == 0 :
                rows = [i + 1 , i + 2]
        
            elif i % 3 == 1 :
                rows = [i - 1 , i + 1]
        
            else :
                rows = [i - 2 , i - 1]
        
            if j % 3 == 0 :
                colomns = [j + 1 , j + 2]
        
            elif j % 3 == 1 :
                colomns = [j - 1 , j + 1]
        
            else :
                colomns = [j - 2 , j - 1]
        
            for row in rows :
                for colomn in colomns :
                    if text == self.cells[row][colomn].text() :
                        self.cells[i][j].setStyleSheet ("background-color: rgb(255, 85, 127); border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-bottom-right-radius: 0px;")
                        self.mistake += 1
                        self.ui.mistakes.setText (str (self.mistake))
                        print("bl", self.mistake)
                        break
        
        # CHECK WIN
        check = 0
        for row in range (9) :
            for colomn in range (9) :
                if self.cells[row][colomn].text() != ""  and self.mistake < 3 :
                    check += 1
        
        if check == 81 :
            txt = "🎉🎉 You WIN 🎉🎉"
            message = QMessageBox (windowTitle = "Congratulation... 🥳" , text = txt)
            message.exec_ ()
            self.new_game ()
        
        # CHECK LOOS
        if self.mistake == 3 :
            txt = "💀💀 You LOOSE 💀💀"
            message = QMessageBox (windowTitle = "Congratulation... 🥴" , text = txt)
            message.exec_ ()
            self.new_game ()


if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = Mainwindow ()
    window.show ()
    app.exec ()