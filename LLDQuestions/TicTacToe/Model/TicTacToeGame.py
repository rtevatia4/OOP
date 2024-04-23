from __future__ import annotations
from PlayingPieceO import PlayingPieceO
from PlayingPieceX import PlayingPieceX
from Board import Board
import PieceType
from Player import Player
import collections


class TicTacToeGame:
    board = None
    queue = collections.deque()

    def initialize_game(self):
        x_piece = PlayingPieceX()
        o_piece = PlayingPieceO()

        player1 = Player("rahul", x_piece)
        player2 = Player("algo", o_piece)

        TicTacToeGame.queue.append(player1)
        TicTacToeGame.queue.append(player2)

        TicTacToeGame.board = Board(3)
    
    def start_game(self):
        winner = False

        while not winner:
            player_turn = TicTacToeGame.queue[0]

            TicTacToeGame.board.print_board()
            free_spaces = TicTacToeGame.board.get_free_cells()

            if not free_spaces:
                winner = True
                continue

            print(f"Player: {player_turn.name}. Enter row and column")
            r, c = map(int, input().split(','))

            is_piece_placed = TicTacToeGame.board.add_piece(r,c, player_turn.playing_piece.piece_type)

            if not is_piece_placed:
                print("Incorret possition chosen, try again")
                continue
            TicTacToeGame.queue.popleft()
            TicTacToeGame.queue.append(player_turn)

            is_someone_won = self.check_winner(r,c,player_turn.playing_piece.piece_type)

            if is_someone_won:
                TicTacToeGame.board.print_board()
                return player_turn.name

        
        return "Tie"
    
    def check_winner(self, row, col, piecetype):
        #check row, column, diagonal, antidiagonal
        row_check = True
        column_check = True
        diag = True
        antiDiag =True
        size = TicTacToeGame.board.size
        game_baord = TicTacToeGame.board.board
        #row check
        for i in range(size):
            if game_baord[row][i] == None or game_baord[row][i] != piecetype:
                row_check = False
        # column check
        for i in range(size):
            if game_baord[i][col] == None or game_baord[i][col] != piecetype:
                column_check = False
        
        #diagonal check
        for i in range(size):
            if game_baord[i][i] == None or game_baord[i][i] != piecetype:
                diag = False
        
        #anti diagonal check
        j = size-1
        for i in range(size):
            if game_baord[i][j] == None or game_baord[i][j] != piecetype:
                antiDiag = False
            j-=1
        
        return row_check or column_check or diag or antiDiag

