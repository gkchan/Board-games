placeholder = ""
o_symbol = "O"
x_symbol = "X"
board_size = 3
player1 = "1"
player2 = "2"


class Board():
    """Creates a game board"""

    def __init__(self):
        """Creates board"""

        self.board = []
        for x in range(board_size):
            self.board.append(board_size*[placeholder])

    def print_board(self):
        """Prints board"""

        for row in self.board:
            for symbol in row:
                print [symbol],
            print "\n"

    def put_symbol(self, symbol, row, column):
        """Put symbol in board"""

        self.board[row][column] = symbol

    def is_empty(self, row, column):
        """Return whether coordinates are empty"""

        return self.board[row][column] == placeholder

    def win_game(self):
        """Returns if game is won"""

        def horizontal_win():
            """Return whether there is horizontal win"""

            for i in range(0, board_size):
                if set(self.board[i]) == set([o_symbol]) or set(self.board[i]) == set([x_symbol]):
                    print "horizontal win"
                    return True

        def vertical_win():
            """Return whether there is vertical win"""

            vert_set = set()
            for i in range(0, board_size):
                for j in range(0, board_size):
                    vert_set.add(self.board[j][i])
                if vert_set == set([o_symbol]) or vert_set == set([x_symbol]):
                    print "vertical win"
                    return True 
                vert_set = set()

        def diagonal_win():
            """Return whether there is diagonal win"""

            diagonal_set = set()
            for i in range(0, board_size):
                diagonal_set.add(self.board[i][i]) 

            # diagonal_set = { self.board[0][0], self.board[1][1], self.board[2][2] }
            if diagonal_set == set([o_symbol]) or diagonal_set == set([x_symbol]):
                print "diagonal win 1"
                return True
            
            diagonal_set = { self.board[0][2], self.board[1][1], self.board[2][0] }
            if diagonal_set == set([o_symbol]) or diagonal_set == set([x_symbol]):
                print "diagonal win 2"
                return True

        if horizontal_win() or vertical_win() or diagonal_win():
            print "You have won."
            return True


    def ask_play_again(self):
        """Asks whether player wants to play again"""

        answer = raw_input("Would you like to play again? Yes/No ")
        if answer == "Yes":
            return True
        elif answer == "No":
            return False
        else:
            return self.ask_play_again()


    def notify_no_win(self):
        """Tells when board is full and no one wins"""

        board_set = set()
        for row in self.board:
            board_set.update(row)
        if "" not in board_set:
            print "Game is over. No one won."
            return True
       


# do while?

def ask_input_helper(player, row_or_column):
    """Ask for player input"""

    try:
        return int(raw_input("Player {}, please choose a {}.".format(player, row_or_column)))
    except ValueError:
        return ask_input_helper(player, row_or_column)


def ask_input(player, row_or_column):
    """Verify input is within range of the board"""

    row_or_column_number = ask_input_helper(player, row_or_column)
    while row_or_column_number not in range(board_size):
        print "Please choose a number within the range."    
        row_or_column_number = ask_input_helper(player, row_or_column)
    return row_or_column_number


def play_game_turn(player, symbol):
    """Play a turn of the game"""

    row = ask_input(player, "row")
    column = ask_input(player, "column")

    if board.is_empty(row, column):
        board.put_symbol(symbol, row, column)
        board.print_board()
    else:
        print "That spot has been taken. Please try again."
        play_game_turn(player, symbol)


def create_new_board():
    """Create a new board from class"""

    board = Board()
    board.print_board()



print "Welcome to your game."

board = Board()
board.print_board()

player1 = raw_input("Player 1, please input your name?") or player1
player2 = raw_input("Player 2, please input your name?") or player2


turn = 1

while True:
    if turn == 1:
        play_game_turn(player1, o_symbol)
        turn = 2
    elif turn == 2:
        play_game_turn(player2, x_symbol)
        turn = 1
    if board.win_game() or board.notify_no_win():
        answer = board.ask_play_again()
        if answer == True:
            board = Board()
            board.print_board()
            continue
        elif answer == False:
            break

# make bigger board
# check win for only new symbols
# change string symbols
# play again
