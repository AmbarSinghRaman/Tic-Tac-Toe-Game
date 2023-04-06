# Tic Tac toe game!
class TicTacToe:
    
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.players = ["X", "O"]
        self.current_player = self.players[0]
        self.winner = None

    def create_board(self, piece_one, piece_two, piece_three, piece_four, piece_five, piece_six, piece_seven, piece_eight, piece_nine):
        print('-------------')
        print("| " + piece_one + " | " + piece_two + " | " + piece_three + " |")
        print('-------------')
        print("| " + piece_four + " | " + piece_five + " | " + piece_six + " |")
        print('-------------')
        print("| " + piece_seven + " | " + piece_eight + " | " + piece_nine + " |")
        print('-------------')

    def instructions(self):
        print('\n\t\t\t\t\t\tTic Tac Toe\n')
        print('As shown below, when making a move type the given number where you would like to place your piece on the board.')
        self.create_board('1', '2', '3', '4', '5', '6', '7', '8', '9')

    def check_win(self):
        if (self.board[0] == self.current_player and self.board[1] == self.current_player and self.board[2] == self.current_player) or \
            (self.board[3] == self.current_player and self.board[4] == self.current_player and self.board[5] == self.current_player) or \
            (self.board[6] == self.current_player and self.board[7] == self.current_player and self.board[8] == self.current_player) or \
            (self.board[0] == self.current_player and self.board[3] == self.current_player and self.board[6] == self.current_player) or \
            (self.board[1] == self.current_player and self.board[4] == self.current_player and self.board[7] == self.current_player) or \
            (self.board[2] == self.current_player and self.board[5] == self.current_player and self.board[8] == self.current_player) or \
            (self.board[0] == self.current_player and self.board[4] == self.current_player and self.board[8] == self.current_player) or \
            (self.board[2] == self.current_player and self.board[4] == self.current_player and self.board[6] == self.current_player):
            return True
        else:
            return False
        
    def play(self):
        self.instructions()
        while self.winner == None:
            current_move = int(input("Enter move from 1 to 9:\n>>> "))
            if self.board[current_move - 1] == ' ':
                self.board[current_move - 1] = self.current_player

                if self.check_win():
                    self.winner = self.current_player

                if " " not in self.board:
                    self.winner = "Tie"

                else:
                    if self.current_player == self.players[0]:
                        self.current_player = self.players[1]

                    else:
                        self.current_player = self.players[0]

            else:
                print('The position you have selected has already been taken!\n')

            self.create_board(self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6], self.board[7], self.board[8])
            
            if self.winner != None:
                if self.winner != 'Tie':
                    print(f'{self.winner} Won!')
                else:
                    print(self.winner)


TicTacToeGame = TicTacToe()
TicTacToeGame.play()
