import numpy as np


def read_input(path):
    with open(path) as f:
        lines = f.read()
    f.close()
    return lines


class Board:
    def __init__(self):
        self.board = np.zeros((5, 5))
        self.bingo_mark = np.zeros((5, 5))

    def input_board(self, line):
        for i in range(len(line)):
            board_lines = [int(b) for b in line[i].split() if b != ""]
            self.board[i] = board_lines

    def mark_input(self, bingo_number):
        if bingo_number in self.board:
            ind = np.where(self.board == bingo_number)
            self.bingo_mark[ind[0], ind[1]] = 1

    def bingo(self):
        return self.bingo_mark.all(axis=0).any() or self.bingo_mark.all(axis=1).any()

    def bingo_score(self, winning_number):
        # print((self.board * (self.bingo_mark == 0)).sum())
        # print((np.multiply(self.board, self.bingo_mark == 0)).sum())
        return (np.multiply(self.board, self.bingo_mark == 0)).sum() * winning_number


def board_score(bingo_numbers, number_of_boards, board):
    for bn in bingo_numbers:
        for b in range(number_of_boards):
            board[b].mark_input(bn)
            if board[b].bingo():
                # print(f"winning board: {b}")
                # print(f"bingo score: {board[b].bingo_score(bn)}")
                return board[b].bingo_score(bn)


# Porblem 2 solution
def last_board_to_win(bingo_numbers, number_of_boards, board):
    board_winning_order = []
    board_winner_and_score = []
    for bn in bingo_numbers:
        for b in range(number_of_boards):
            board[b].mark_input(bn)
            if board[b].bingo():
                if b not in board_winning_order:
                    board_winning_order.append(b)
                    board_winner_and_score.append([b, board[b].bingo_score(bn)])

    # print(f"board_winning_order: {board_winning_order}")
    return (board_winning_order[-1], board_winner_and_score[-1][1])


input_path = "day_4/input.txt"
test_input_path = "day_4/test_input.txt"
input = read_input(input_path).split("\n")
# print(input)

bingo_numbers = [int(bn) for bn in input[0].split(",")]
# print(bingo_numbers)

number_of_boards = (len(input) - 1) // 6
print(f"number of boards: {number_of_boards}")

board = dict()

for j in range(number_of_boards):
    board[j] = Board()
    # print(f"start of board {j} is: {2+(j*6)}")
    # print(f"end of board {j} is: {2+(j*6)+4}")
    board[j].input_board(input[2 + (j * 6) : (7 + (j * 6))])


print(f"board_Score: {board_score(bingo_numbers, number_of_boards, board)}")

last_winning_board, lb_score = last_board_to_win(bingo_numbers, number_of_boards, board)
print(f"last winning board: {last_winning_board}")
print(f"last board to win score: {lb_score}")
