class Board():
    """Creates a game board"""

    def __init__(self):
        """Creates board"""

        self.board = []
        for x in range(3):
            self.board.append(3*[[]])
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

        return self.board[row][column] == []


row = raw_input("Player 1, please choose a row.")
column = raw_input("Player 1, please choose a column.")

# board = Board()
# board.print_board()
# board.put_symbol("O", 0, 1)
# board.print_board()
# print board.is_empty(1,1)
# print board.is_empty(0,1)

