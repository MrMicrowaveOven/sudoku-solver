# The old method, which uses a .txt graphic

import sys
sys.path.append("lib")

from board import Board

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

parse_board_old(board_old).attempt_to_solve()
