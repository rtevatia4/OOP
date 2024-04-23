import PlayingPiece

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for c in range(self.size)] for r in range(self.size)]
    
    def add_piece(self, row, col, piece):
        if not (row in range(self.size) and col in range(self.size)):
            return False
        
        if self.board[row][col] != None:
            return False
        
        self.board[row][col] = piece
        return True
    
    def get_free_cells(self):
        free = []
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == None:
                    free.append((r,c))
        
        return free
    
    def print_board(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] != None:
                    print(self.board[r][c].name + "  ", end="")
                else:
                    print("  ", end="")
                print(" | ", end="")
            print()
                

            