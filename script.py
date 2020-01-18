# The new method, which uses a copy/paste of an excel document
# Make sure to put ' ' in empty cells, otherwise it won't copy them.
import sys
sys.path.append("lib")

from board import Board

def parse_board(board):
    board_arr = board.split("\n")
    new_board_arr = []
    for row in board_arr:
        if len(row) == 0:
            break
        row_array = []
        for i, space in enumerate(row):
            if i % 2 == 0:
                if space == ' ':
                    row_array.append(None)
                else:
                    row_array.append(int(space))
        while len(row_array) < 9:
            row_array.append(None)
        new_board_arr.append(row_array)
    print new_board_arr
    return Board(new_board_arr)

with open('board.txt', 'r') as file:
    board_array = file.read()

parse_board(board_array)
# .attempt_to_solve()
