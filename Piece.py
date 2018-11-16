


class Piece:
    def __init__(self,let,num,type):
        '''Initialise info arrays'''
        self.lets = ['A','B','C','D','E','F','G','H']
        self.nums = ['8','7','6','5','4','3','2','1']
        self.piece_ids = ['P','R','N','B','Q','K','p','r','n','b','q','k']
        '''Set assertions'''
        assert isinstance(let,str), "Letter is not string type: %s" % let
        assert isinstance(num,str), "Number is not string type: %s" % num
        assert let in self.lets, "Letter is not a valid letter coordinate: %s" % let
        assert num in self.nums, "Number is not a valid number coordinate: %s" % num
        '''Set variables'''
        self.let = let
        self.num = num
        self.type = type

    def __str__(self):
        return self.type

    def move(let,num):
        #if possible
        self.let = let
        self.num = num

    def check_move_general(self):
        #not onto own piece
        #not invalid cooridinate
        return
