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

    # def is_valid(self, index):
    #     """Check if index is valid"""

        # if index not in range(3):

    def win_game(self):
        """Returns if game is won"""

        def horizontal_win():
            """Return whether there is horizontal win"""

            # if "" not in board.board[0]
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

            diagonal_set = { self.board[0][0], self.board[1][1], self.board[2][2] }
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


    def notify_no_win(self):
        """Tells when board is full and no one wins"""

        board_set = set()
        for row in self.board:
            board_set.update(row)
            # print row, board_set
        if "" not in board_set:
            play_again = raw_input("Game is over. No one won. Would you like to play again? Yes/No ")
            if play_again == "Yes":
                return True
            elif play_again == "No":
                return False
            else:
                notify_no_win(self)







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

    # row, column = None, None

    row = ask_input(player, "row")
    column = ask_input(player, "column")

    if board.is_empty(row, column):
        board.put_symbol(symbol, row, column)
        board.print_board()
    else:
        print "That spot has been taken. Please try again."
        play_game_turn(player, symbol)


print "Welcome to your game."

board = Board()
board.print_board()

def create_new_board():
    """Create a new board from class"""

    board = Board()
    board.print_board()

# create_new_board()

# print notify_no_win

player1 = raw_input("Player 1, please input your name?") or player1
player2 = raw_input("Player 2, please input your name?") or player2

# def play_game():
#     """Play game"""

while True:  
    play_game_turn(player1, o_symbol)
    if board.win_game():
        break
    replay = board.notify_no_win()
    if replay == True:
        board = Board()
        board.print_board()
        # create_new_board()
        # play_game()
        continue
    elif replay == False:
        break
    play_game_turn(player2, x_symbol)
    if board.win_game():
        break
    replay = board.notify_no_win()
    if replay == True:
        board = Board()
        board.print_board()
        # create_new_board()
        # play_game()
        continue
    elif replay == False:
        break
       

# play_game()






# change string symbols
# empty row, column bug
# game over
# no win
# replay?
# win, play again
