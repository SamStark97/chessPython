"IMPORT USER MODULES"
import pieces

"IMPORT PRO MODULES"
import pandas as pd

"CONSTANTS"
WHITE = 0
BLACK = 1
COLUMNS = ['A','B','C', 'D', 'E', 'F', 'G', 'H']

def get_coords(board_file, board_rank):
    return COLUMNS.index(board_file, 9-board_rank)


class Board(object):

    def __init__(self):
        self._board = pd.DataFrame(columns=COLUMNS, index=[8,7,6,5,4,3,2,1])
        self._turn = WHITE
        self._castling = (0, 0)

    def get_piece(self, board_file, board_rank):
        return self._board.loc[board_rank, board_file]

    def testing(self):
        self._board.loc[3, 'B'] = pieces.Pawn(BLACK, 'B', 3)
        print(self._board)

    def initialise_board(self):

        "empty spaces"
        self._board.loc[[3,4,5,6]] = None

        "pawns"
        for board_file in self._board.columns.values:
            self._board.loc[2] = pieces.Pawn(WHITE, board_file, 2)
            self._board.loc[7] = pieces.Pawn(BLACK, board_file, 7)

        "rooks"
        self._board.loc[1, 'A'] = pieces.Rook(WHITE, 'A', 1)
        self._board.loc[8, 'A'] = pieces.Rook(BLACK, 'A', 8)
        self._board.loc[1, 'H'] = pieces.Rook(WHITE, 'H', 1)
        self._board.loc[8, 'H'] = pieces.Rook(BLACK, 'H', 8)

        "knights"
        self._board.loc[1, 'B'] = pieces.Knight(WHITE, 'B', 1)
        self._board.loc[8, 'B'] = pieces.Knight(BLACK, 'B', 8)
        self._board.loc[1, 'G'] = pieces.Knight(WHITE, 'G', 1)
        self._board.loc[8, 'G'] = pieces.Knight(BLACK, 'G', 8)

        "bishops"
        self._board.loc[1, 'C'] = pieces.Bishop(WHITE, 'C', 1)
        self._board.loc[8, 'C'] = pieces.Bishop(BLACK, 'C', 8)
        self._board.loc[1, 'F'] = pieces.Bishop(WHITE, 'F', 1)
        self._board.loc[8, 'F'] = pieces.Bishop(BLACK, 'F', 8)

        "queens"
        self._board.loc[1, 'D'] = pieces.Queen(WHITE, 'D', 1)
        self._board.loc[8, 'D'] = pieces.Queen(BLACK, 'D', 8)

        "kings"
        self._board.loc[1, 'E'] = pieces.King(WHITE, 'E', 1)
        self._board.loc[8, 'E'] = pieces.King(BLACK, 'E', 8)

        print(self._board)

    def check_collision(self, start_pos, end_pos, direction):
        "check if piece in the way"

    def move_piece(self, start_pos, end_pos):
        "check if valid move then move it, update GUI"

        piece = self.get_piece(*start_pos)
        end_object = self.get_piece(*end_pos)

        "Check that piece exists"
        if piece == None:
            return

        "Check if correct piece for turn"
        if piece._team != self._turn:
            return

        if end_object == None:
            enemy_piece_at_end = False
        else:
            enemy_piece_at_end = True

        valid = piece.move_piece(start_pos, end_pos, enemy_piece_at_end)
        print('Move is valid? | ', valid)
        if valid == False:
            return

        self._board.loc[end_pos[1], end_pos[0]] = piece
        self._board.loc[start_pos[1], start_pos[0]] = None



        print(self._board)

    def get_board(self):
        return self._board
