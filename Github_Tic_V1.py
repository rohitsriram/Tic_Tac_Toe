import Game_Player
import AI_Player

class Game_Board(object):

    def __init__(self):
        self.game_board = [[0,0,0],[0,0,0],[0,0,0]]
        self.display_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player_turn = 1


    def show_board(self, display_board):
        for i in display_board:
            print(i)

    def update_board(self, display_board, move, player):
        row = int(move[0])
        col = int(move[2])

        self.game_board[row][col] = player.id
        if (self.player_turn == 1):
            player.row[row] += 1
            player.col[col] += 1
            display_board[row][col] = "O"
            self.player_turn += 1
        elif (self.player_turn == 2):
            player.row[row] += 1
            player.col[col] += 1
            display_board[row][col] = "X"
            self.player_turn -= 1

    def get_game_board(self):
        return self.game_board

    def is_row_matched(self, player):
        for key, value in player.row.items():
            if value == 3:
                return True

        return False

    def is_col_matched(self, player):
        for key, value in player.col.items():
            if value == 3:
                return True

        return False

    def diag(self, player):
        center = self.game_board[1][1] == player.id
        corner1 = self.game_board[0][0] == player.id
        corner2 = self.game_board[2][2] == player.id
        corner3 = self.game_board[0][2] == player.id
        corner4 = self.game_board[2][0] == player.id

        if corner1 and center and corner2:
            return True
        elif corner3 and center and corner4:
            return True
        return False

    def tie(self, player1, player2):
        sum = 0
        for i in player1.row:
            sum += player1.row[i]

        for j in player2.row:
            sum += player2.row[j]

        if sum == 9:
            return True
        else:
            return False

    def win(self, player):
        row_match = self.is_row_matched(player)
        col_match = self.is_col_matched(player)
        diag_match = self.diag(player)

        if row_match or col_match or diag_match:
            return True
        else:
            return False


    def main(self):
        board = Game_Board()
        player1 = Game_Player.MyPlayer(1)
        player2 = AI_Player.Ai_Player(2)
        board.show_board(board.display_board)
        while True:

            first_input = player1.get_input(board)
            board.update_board(board.display_board, first_input, player1)
            board.show_board(board.display_board)
            if board.win(player1):
                print("Player 1 won!")
                break
            elif board.tie(player1, player2):
                print("Game is a tie!")
                break

            second_input = player2.get_move(board, player1)
            board.update_board(board.display_board, second_input, player2)
            board.show_board(board.display_board)
            if board.win(player2):
                print("Player 2 won")
                break
            elif board.tie(player1, player2):
                print("Game is a tie!")
                break



if __name__ == '__main__':
    Game_Board().main()
