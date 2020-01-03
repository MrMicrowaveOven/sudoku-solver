import sys
sys.path.append("lib")

from board import Board

b = Board()
b.fill_space([1,2],5)
b.fill_space([1,1],4)
b.show_board()
