import sys
sys.path.append("lib")

from board import Board

# The new method, which uses a copy/paste of an excel document
# Make sure to put ' ' in empty cells, otherwise it won't copy them.

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
    return Board(new_board_arr)

with open('board.txt', 'r') as file:
    board = file.read()

parse_board(board).attempt_to_solve()

# The old method, which uses a .txt graphic

with open('board_old.txt', 'r') as file:
    board_old = file.read()

def parse_board_old(board):
    board_arr = board.split("\n")
    board_arr = board_arr[2:13]
    board_arr = board_arr[0:3] + board_arr[4:7] + board_arr[8:11]
    value_array = []
    for row in board_arr:
        row_arr = []
        for index in [2,4,6,8,10,12,14,16,18]:
            row_arr.append(row[index])
        value_array.append(row_arr)

    for row_array in value_array:
        for i,value in enumerate(row_array):
            if value == ' ':
                row_array[i] = None
            else:
                row_array[i] = int(value)
    # print value_array
    return Board(value_array)
