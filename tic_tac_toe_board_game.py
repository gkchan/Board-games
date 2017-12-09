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


board = Board()
board.print_board()


while True: 
    row = int(raw_input("Player 1, please choose a row."))
    column = int(raw_input("Player 1, please choose a column."))
    if board.is_empty(row, column):
        board.put_symbol("O", row, column)
        board.print_board()
    else:
        pass
    # row = int(raw_input("Player 2, please choose a row."))
    # column = int(raw_input("Player 2, please choose a column."))
    # if board.is_empty(row, column):
    #     board.put_symbol("X", row, column)
    #     board.print_board()
        

    # horizontal win:
    # # if "" not in board.board[0]
    # print set(board.board[0])
    # for i in range(0, 3):
    #     if set(board.board[i]) == set(["O"]) or set(board.board[i]) == set(["X"]):
    #         print "win"


    # vert_set = set()
    # for i in range(0, 3):
    #     for j in range(0, 3):
    #         vert_set.add(board.board[j][i])
    #     print vert_set
    #     if vert_set == set(["O"]) or vert_set == set(["X"]):
    #         print "vertical win"
    #     vert_set = set()

    diagonal_set = set()
    diagonal_set.add(board.board[0][0])
    diagonal_set.add(board.board[1][1])
    diagonal_set.add(board.board[2][2])
    if diagonal_set == set(["O"]) or diagonal_set == set(["X"]):
        print "diagonal win"

    





  
    






