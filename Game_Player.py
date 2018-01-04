class MyPlayer(object):

    def __init__(self, id):
        self.row = {0: 0, 1: 0, 2: 0}
        self.col = {0: 0, 1: 0, 2: 0}
        self.id = id

    def get_input(self, board):
        while True:
            print("What is your move?")
            user_input = input()
            acceptable = self.verify_input(user_input, board)
            if acceptable:
                return user_input
            else:
                print("Invalid move. Try Again")


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


    def get_id(self):
        return self.id