"IMPORT USER MODULES"
import board

"IMPORT PRO MODULES"
import os
import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image

"CONSTANTS"
PIECE_NAMES = ['pawnWhite','knightWhite','bishopWhite','rookWhite','queenWhite','kingWhite',
               'pawnBlack','knightBlack','bishopBlack','rookBlack','queenBlack','kingBlack']
COLUMNS = ['A','B','C', 'D', 'E', 'F', 'G', 'H']


def import_pieces(rel_path):
    return [ImageTk.PhotoImage(Image.open(rel_path + f + '.png')) for f in PIECE_NAMES]


class ChessGUI(tk.Frame):
    def __init__(self, parent, squareWidth=64, squareHeight=64):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.images = import_pieces('piece_images\\')
        self.squareWidth = squareWidth
        self.squareHeight = squareHeight
        self.width = 8 * squareWidth
        self.height = 8 * squareHeight
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.buttons = {}

        colours = ['AntiqueWhite1', 'gray23']
        for column, col_name in enumerate(COLUMNS):
            self.buttons[col_name] = {}
            for row in range(1,9):
                #self.canvas.create_rectangle(squareWidth*row, squareWidth*column,
                #                             squareWidth * (row + 1), squareWidth * (column + 1),
                #                             fill=colours[(column + row) % 2])
                self.buttons[col_name][row] = tk.Button(self.canvas, command=self.sayhi,
                                                 bg=colours[(column + row-1) % 2] ,
                                                 height=self.squareHeight,width=self.squareWidth,
                                                 relief=tk.FLAT, bd=0)
                self.buttons[col_name][row].place(x=(self.squareWidth * (column)), y=(self.squareWidth * (row-1)))
                #print(squareWidth * (row + 0.5), squareWidth * (column + 0.5))
                #self.canvas.create_window(squareWidth * (row + 0.5), squareWidth * (column + 0.5),
                #                          window=self.buttons[column][row])


        #img = self.images[0]
        #self.canvas.create_image(squareWidth/2, self.height - (squareHeight) + squareHeight/2, image=img)
        #self.buttons[1][0].config(image=self.images[0])
        #self.canvas.pack()


    def place_pieces(self, current_board):
        "hello"
        for file_ in current_board.columns.values:
            for rank_ in range(1,9):
                #print(current_board.loc[rank_, file_],type(str(current_board.loc[rank_, file_])))

                if str(current_board.loc[rank_, file_]) == 'wRook':
                    self.buttons[file_][9 - rank_].config(image=self.images[3])
                elif str(current_board.loc[rank_, file_]) == 'bRook':
                    self.buttons[file_][9 - rank_].config(image=self.images[9])
                elif str(current_board.loc[rank_, file_]) == 'wKnight':
                    self.buttons[file_][9 - rank_].config(image=self.images[1])
                elif str(current_board.loc[rank_, file_]) == 'bKnight':
                    self.buttons[file_][9 - rank_].config(image=self.images[7])
                elif str(current_board.loc[rank_, file_]) == 'wPawn':
                    self.buttons[file_][9 - rank_].config(image=self.images[0])
                elif str(current_board.loc[rank_, file_]) == 'bPawn':
                    self.buttons[file_][9 - rank_].config(image=self.images[6])
                elif str(current_board.loc[rank_, file_]) == 'wKing':
                    self.buttons[file_][9 - rank_].config(image=self.images[5])
                elif str(current_board.loc[rank_, file_]) == 'bKing':
                    self.buttons[file_][9 - rank_].config(image=self.images[11])
                elif str(current_board.loc[rank_, file_]) == 'wQueen':
                    self.buttons[file_][9 - rank_].config(image=self.images[4])
                elif str(current_board.loc[rank_, file_]) == 'bQueen':
                    self.buttons[file_][9 - rank_].config(image=self.images[10])
                elif str(current_board.loc[rank_, file_]) == 'wBishop':
                    self.buttons[file_][9 - rank_].config(image=self.images[2])
                elif str(current_board.loc[rank_, file_]) == 'bBishop':
                    self.buttons[file_][9 - rank_].config(image=self.images[8])
                else:
                    self.buttons[file_][9 - rank_].config(image='')

        self.canvas.pack()
        self.pack()


    def sayhi(self):
        print("hello")
