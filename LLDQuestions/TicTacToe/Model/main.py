from TicTacToeGame import TicTacToeGame
def main():
    game = TicTacToeGame()
    game.initialize_game()
    print("Winner is:", game.start_game())

if __name__ == "__main__":
    main()