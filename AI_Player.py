import random

class Ai_Player(object):

    def __init__(self, id):
        self.row = {0: 0, 1: 0, 2: 0}
        self.col = {0: 0, 1: 0, 2: 0}
        self.blocked_rows = []
        self.blocked_cols = []
        self.row_block = False
        self.col_block = False
        self.diag_block = False
        self.id = id

    def get_move(self, board, player):
        print("AI's turn")
        while True:
            row = self.block_row(player)
            col = self.block_col(player)
            move = str(row) + ' ' + str(col)
            acceptable = self.verify_input(move, board)
            if acceptable:
                if self.row_block:
                    self.blocked_rows.append(row)
                    self.row_block = False
                if self.col_block:
                    self.blocked_cols.append(col)
                    self.col_block = False
                return move


    def block_row(self, player):
        for key, value in player.row.items():
            row_full = (self.row[key] + value) == 3
            if value == 2 and not row_full:
                if not(key in self.blocked_rows):
                    self.row_block = True
                    return key
        return random.randint(0, 2)

    def block_col(self, player):
        for key, value in player.col.items():
            col_full = (self.col[key] + value) == 3
            if value == 2 and not col_full:
                if not(key in self.blocked_cols):
                    if not self.row_block:
                        self.col_block = True
                        return key

        return random.randint(0, 2)

    def verify_input(self, test_input, board):
        if len(test_input) < 3:
            return False
        first_valid = int(test_input[0]) in range(0,3)
        second_valid = int(test_input[2]) in range(0,3)
        valid = first_valid and second_valid
        return valid and self.not_repeat_move(test_input, board)

    def not_repeat_move(self, test_input, board):
        row = int(test_input[0])
        col = int(test_input[2])
        return board.game_board[row][col] == 0