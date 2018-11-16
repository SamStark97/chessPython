import pandas as pd




class Board:
    def __init__(self):
        self.board = pd.DataFrame(columns=['8','7','6','5','4','3','2','1'],index=['A','B','C','D','E','F','G','H']);

    def show_board(self):
        print(self.board)
