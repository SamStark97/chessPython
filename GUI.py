from Board import Board
from Piece import *
import tkinter as tk
from PIL import Image, ImageTk

'''
# TODO:
exit
fix piece and board scaling
turn label
'''

class Chess_GUI(tk.Frame):

    selected = None
    selected_piece = None
    hilighted = None

    def __init__(self,parent,board):
        self.parent = parent
        self.board = board
        tk.Frame.__init__(self, parent)
        self.board_lets = ['A','B','C','D','E','F','G','H']
        self.board_nums = ['8','7','6','5','4','3','2','1']

        self.cols = 8
        self.rows = 8
        self.sqr_size = 60
        self.colour1 = 'white'
        self.colour2 = 'grey'
        self.piece_dir = 'piece_images'
        #ImageTk.PhotoImage(Image.open("True1.gif"))
        pieces = [ImageTk.PhotoImage(Image.open('piece_images/pawnWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/rookWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/knightWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/bishopWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/queenWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/kingWhite.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/pawnBlack.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/rookBlack.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/knightBlack.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/bishopBlack.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/queenBlack.png')), \
                            ImageTk.PhotoImage(Image.open('piece_images/kingBlack.png'))]
        self.piece_dic = {'P':pieces[0], \
                            'R':pieces[1], \
                            'N':pieces[2], \
                            'B':pieces[3], \
                            'Q':pieces[4], \
                            'K':pieces[5], \
                            'p':pieces[6], \
                            'r':pieces[7], \
                            'n':pieces[8], \
                            'b':pieces[9], \
                            'q':pieces[10], \
                            'k':pieces[11]}

        canvas_height = self.rows * self.sqr_size
        canvas_width = self.cols * self.sqr_size

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack(side="top", fill="both", expand="true", padx=4, pady=4)

        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.click)


    def refresh(self, event={}):
        self.canvas.delete("square")
        self.canvas.delete("piece")
        for x in range(self.cols):
            for y in range(self.rows):
                colour = self.colour2 if (x+y)%2 == 0 else self.colour1
                x0 = (x)*self.sqr_size
                y0 = (y)*self.sqr_size
                x1 = x0 + self.sqr_size
                y1 = y0 + self.sqr_size
                if (self.selected_piece is not None) and (self.board_lets[x],self.board_nums[y]) == self.selected_piece:
                    self.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill='orange', tags="square")
                elif (self.selected is not None) and (self.board_lets[x],self.board_nums[y]) in self.selected:
                    self.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill='spring green', tags="square")
                else:
                    self.canvas.create_rectangle(x0,y0,x1,y1, outline="black", fill=colour, tags="square")

        for k,v in self.board.get_piece_info().items():
            for i in v:
                x2 = self.sqr_size * self.board_lets.index(i[0]) + int(self.sqr_size/2)
                y2 = self.sqr_size * self.board_nums.index(i[1]) + int(self.sqr_size/2)
                self.canvas.create_image(x2,y2, image=self.piece_dic[k], tags=(k, "piece"), anchor="c")

        self.canvas.tag_lower('square')
        self.canvas.tag_raise('piece')
        self.canvas.pack(fill="both", expand=True)

    def hilight(self, coords):
        piece = self.board.get_pos_info(coords[0],coords[1])
        if type(piece) != str and piece.get_side() == self.board.get_turn():
            self.selected_piece = coords
            self.selected = piece.get_moves()
            print (self.selected)

    def click(self, event):
        col_size = row_size = event.widget.master.sqr_size
        cur_col = int(event.x / col_size)
        cur_row = int(event.y / row_size)
        coords = (self.board_lets[cur_col],self.board_nums[cur_row])

        if self.selected_piece:
            if self.board.move(self.selected_piece[0],self.selected_piece[1],coords[0],coords[1]):
                self.selected_piece = None
                self.selected = None
                self.hilighted = None

        self.hilight(coords)
        self.refresh()
        self.board.show_board()
