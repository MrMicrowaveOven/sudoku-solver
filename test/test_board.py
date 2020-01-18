import sys
sys.path.append("../lib")

import unittest

from board import Board
from space import Space

class BoardTest(unittest.TestCase):
    def test_board_array(_):
        b = Board()
        b.fill_space([1,2], 4)
        b.fill_space([1,3], 5)
        board_arr = b.board_array()
        correct_board_array = [
            [None, None, None, None, None, None, None, None, None],
            [None, None, 4, 5, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
        ]
        _.assertEquals(board_arr, correct_board_array)

    def test_get_vert_spaces(_):
        b = Board()
        vert_spaces = [
            [0,2],
            [2,2],
            [3,2],
            [4,2],
            [5,2],
            [6,2],
            [7,2],
            [8,2],
        ]
        _.assertEquals(b.get_vert_spaces([1,2]), vert_spaces)

    def test_get_hor_spaces(_):
        b = Board()
        hor_spaces = [
            [1,0],
            [1,1],
            [1,3],
            [1,4],
            [1,5],
            [1,6],
            [1,7],
            [1,8],
        ]
        _.assertEquals(b.get_hor_spaces([1,2]), hor_spaces)

    def test_get_block_spaces(_):
        b = Board()
        block_spaces = [
            [0,6],[0,7],[0,8],
            [1,6],[1,8],
            [2,6],[2,7],[2,8]
        ]
        _.assertEquals(b.get_block_spaces([1,7]), block_spaces)
    def test_get_eliminating_values(_):
        b = Board()
        b.fill_space([1,2],5)
        b.fill_space([1,1],4)
        b.fill_space([0,4],6)
        b.fill_space([5,3],6)
        b.fill_space([7,3],7)
        eliminating_values = [4,5,6,7]
        _.assertEquals(b.get_eliminating_values([1,3]), eliminating_values)

    def test_attempt_to_guess_space(_):
        b = Board()
        b.fill_space([0,5],1)
        b.fill_space([1,5],2)
        b.fill_space([2,5],3)
        b.fill_space([1,1],4)
        b.fill_space([1,2],5)
        b.fill_space([0,4],6)
        b.fill_space([5,3],6)
        b.fill_space([7,3],7)
        b.fill_space([1,6],9)
        b.attempt_to_guess_space([1,3])
        _.assertEquals(b.get_space([1,3]).value, 8)

if __name__ == "__main__":
    unittest.main()
