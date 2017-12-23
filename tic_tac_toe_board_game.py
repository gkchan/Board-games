class Board():
    """Creates a game board"""

    def __init__(self):
        """Creates board"""

        self.board = []
        for x in range(3):
            self.board.append(3*[""])

    def print_board(self):
        """Prints board"""

        for row in self.board:
            print row

    def put_symbol(self, symbol, row, column):
        """Put symbol in board"""

        self.board[row][column] = symbol

    def is_empty(self, row, column):
        """Return whether coordinates are empty"""

        return self.board[row][column] == ""

    # def is_valid(self, index):
    #     """Check if index is valid"""

        # if index not in range(3):

    def win_game(self):
        """Returns if game is won"""

        def horizontal_win():
            """Return whether there is horizontal win"""

            # if "" not in board.board[0]
            print set(self.board[0])
            for i in range(0, 3):
                if set(self.board[i]) == set(["O"]) or set(self.board[i]) == set(["X"]):
                    print "horizontal win"
                    return True

        def vertical_win():
            """Return whether there is vertical win"""

            vert_set = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    vert_set.add(self.board[j][i])
                print vert_set
                if vert_set == set(["O"]) or vert_set == set(["X"]):
                    print "vertical win"
                    return True
                    
                vert_set = set()

        def diagonal_win():
            """Return whether there is diagonal win"""

            diagonal_set = { self.board[0][0], self.board[1][1], self.board[2][2] }
            if diagonal_set == set(["O"]) or diagonal_set == set(["X"]):
                print "diagonal win 1"
                return True
            
            diagonal_set = { self.board[0][2], self.board[1][1], self.board[2][0] }
            if diagonal_set == set(["O"]) or diagonal_set == set(["X"]):
                print "diagonal win 2"
                return True

        if horizontal_win() or vertical_win() or diagonal_win():
            print "You have won."
            return True



# do while?

def ask_input(player, row_or_column):
    """Ask for player input"""

    row_or_column = int(raw_input("Player {}, please choose a {}.".format(player, row_or_column)))
    while row_or_column not in range(3):
        print "Please choose a number within the range."    
        row_or_column = int(raw_input("Player {}, please choose a {}.".format(player, row_or_column)))
    return row_or_column


def play_game_turn(player, symbol):
    """Play a turn of the game"""

    row, column = None, None

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

# player1 = raw_input("Player 1, please input your name?")

while True:  
    play_game_turn("1", "O")
    if board.win_game():
        break
    play_game_turn("2", "X")
    if board.win_game():
        break


