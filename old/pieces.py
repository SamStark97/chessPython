


"CONSTANTS"
LEGAL = True
ILLEGAL = False
FILES = ['A','B','C', 'D', 'E', 'F', 'G', 'H']

def general_check_legal_move(start, end):
    "Check king checks"
    return LEGAL

class Pawn(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wPawn'
        else:
            return 'bPawn'

    def move_piece(self, start, end, enemy_piece_at_end):
        move_is_legal = LEGAL

        "check king checks"
        move_is_legal = general_check_legal_move(start, end)

        "check movements"
        if start[0] == end[0]:
            if not ((end[1] == (start[1] + 1)) or (end[1] == (start[1] + 2) and start[1] == (5 * self._team + 2))):
                move_is_legal = ILLEGAL
        elif (FILES.index(start[0]) == FILES.index(end[0]) + 1) or (FILES.index(start[0]) == FILES.index(end[0]) - 1):
            if end[1] != (start[1] + 1) or enemy_piece_at_end == False:
                move_is_legal = ILLEGAL
        else:
            move_is_legal = ILLEGAL

        "change pos if move is legal"
        if move_is_legal == LEGAL:
            self._position = end

        return move_is_legal

class Knight(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wKnight'
        else:
            return 'bKnight'

class Bishop(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wBishop'
        else:
            return 'bBishop'

class Rook(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wRook'
        else:
            return 'bRook'

class Queen(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wQueen'
        else:
            return 'bQueen'

class King(object):
    def __init__(self, team, board_file, board_rank):
        self._position = (board_file, board_rank)
        self._team = team

    def __str__(self):
        if self._team == 0:
            return 'wKing'
        else:
            return 'bKing'
