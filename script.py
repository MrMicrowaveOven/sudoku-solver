import sys
sys.path.append("lib")


from board import Board

b = Board()
b.fill_space([1,2],5)
b.fill_space([1,1],4)
# b.show_board()

def parse_board(board):
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

with open('board.txt', 'r') as file:
    board = file.read()

parsed_board = parse_board(board)
parsed_board.show_board()
# board = '
#   0 1 2 3 4 5 6 7 8
#  -------------------
# 0|     |     |     |
# 1|  4 5|     |     |
# 2|     |     |     |
#  -------------------
# 3|     |     |     |
# 4|     |     |     |
# 5|     |     |     |
#  -------------------
# 6|     |     |     |
# 7|     |     |     |
# 8|     |     |     |
#  -------------------
# '
