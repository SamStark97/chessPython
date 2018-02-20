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
        for column in range(8):
            self.buttons[column] = {}
            for row in range(8):
                #self.canvas.create_rectangle(squareWidth*row, squareWidth*column,
                #                             squareWidth * (row + 1), squareWidth * (column + 1),
                #                             fill=colours[(column + row) % 2])
                self.buttons[column][row] = tk.Button(self.parent, command=self.sayhi,
                                                 bg=colours[(column + row) % 2] ,
                                                 height=self.squareHeight,width=self.squareWidth,
                                                 relief=tk.FLAT,  bd=0)
                self.buttons[column][row].place(x=(self.squareWidth * row), y=(self.squareWidth * column))
                #print(squareWidth * (row + 0.5), squareWidth * (column + 0.5))
                #self.canvas.create_window(squareWidth * (row + 0.5), squareWidth * (column + 0.5),
                #                          window=self.buttons[column][row])


        #img = self.images[0]
        #self.canvas.create_image(squareWidth/2, self.height - (squareHeight) + squareHeight/2, image=img)
        self.buttons[1][0].config(image=self.images[0])
        self.canvas.pack()


    def place_pieces(self, current_board):
        "hello"
        #img = ImageTk.PhotoImage(Image.open('pawnWhite.png'))
        #self.canvas.create_image(400,400, image=img, state=tk.NORMAL, anchor=tk.NW)
        #self.canvas.pack()
        #panel = tk.Label(self, image = img)
        #panel.pack(side = "bottom")

    def sayhi(self):
        print("hello")
