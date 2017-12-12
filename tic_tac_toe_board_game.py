class Board():
    """Creates a game board"""

    def __init__(self):
        """Creates board"""

        self.board = []
        for x in range(3):
            self.board.append(3*[""])
        # for row in self.board:
        #     print row

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

        # win = False

        # horizontal win:
        # if "" not in board.board[0]
        print set(self.board[0])
        for i in range(0, 3):
            if set(self.board[i]) == set(["O"]) or set(self.board[i]) == set(["X"]):
                print "win"
                return True

        vert_set = set()
        for i in range(0, 3):
            for j in range(0, 3):
                vert_set.add(self.board[j][i])
            print vert_set
            if vert_set == set(["O"]) or vert_set == set(["X"]):
                print "vertical win"
                return True
                
            vert_set = set()

        diagonal_set = set()
        diagonal_set.add(self.board[0][0])
        diagonal_set.add(self.board[1][1])
        diagonal_set.add(self.board[2][2])
        if diagonal_set == set(["O"]) or diagonal_set == set(["X"]):
            print "diagonal win"
            return True
        
        diagonal_set = set()
        diagonal_set.add(self.board[0][2])
        diagonal_set.add(self.board[1][1])
        diagonal_set.add(self.board[2][0])
        if diagonal_set == set(["O"]) or diagonal_set == set(["X"]):
            print "diagonal win"
            return True






board = Board()
board.print_board()
row = None
column = None

# do while?

while True: 
    row = int(raw_input("Player 1, please choose a row."))
    while row not in range(3):
        # print "Input not valid"
        row = int(raw_input("Player 1, please choose a row."))

    column = int(raw_input("Player 1, please choose a column."))
    while column not in range(3):
        column = int(raw_input("Player 1, please choose a column."))
    if board.is_empty(row, column):
        board.put_symbol("O", row, column)
        board.print_board()
    else:
        pass

    if board.win_game():
        print "You have won."
        break

    row = int(raw_input("Player 2, please choose a row."))
    while row not in range(3):
        row = int(raw_input("Player 2, please choose a row."))
    
    column = int(raw_input("Player 2, please choose a column."))
    while column not in range(3):
        column = int(raw_input("Player 2, please choose a column."))
    if board.is_empty(row, column):
        board.put_symbol("X", row, column)
        board.print_board()

    if board.win_game():
        print "You have won."
        break
        

  






  
    







