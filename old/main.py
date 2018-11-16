
import board
import gui
import tkinter as tk

'''
Steps:
Initialise objects

'''

chess_board = board.Board()
chess_board.initialise_board()

root = tk.Tk()
gui = gui.ChessGUI(root)
gui.place_pieces(chess_board.get_board())

#board.testing()
chess_board.move_piece(('A', 2), ('A', 3))
gui.place_pieces(chess_board.get_board())
#chess_board.move_piece(('B', 3), ('A', 5))

tk.mainloop()
