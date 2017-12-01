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

    def put_symbol(self, symbol, x, y):
        """Put symbol in board"""

        self.board[x][y] = symbol

    def is_empty(self, x, y):
        """Return whether coordinates are empty"""

        return self.board[x][y] == []



board = Board()
board.print_board()
board.put_symbol("O", 0, 1)
board.print_board()
print board.is_empty(1,1)
print board.is_empty(0,1)

