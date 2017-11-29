class Board():
    """Creates a game board"""

    def __init__(self):
        """Creates board"""

        self.board = []
        for x in range(3):
            self.board.append(3*[[]])
        for row in self.board:
            print row

    def print_board(self):
        """Prints board"""

        for row in self.board:
            print row


board = Board()
board.print_board()