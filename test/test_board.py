import sys
sys.path.append("../lib")

import unittest

from board import Board
from space import Space

class BoardTest(unittest.TestCase):
    def test_is_invalid_with_row(_):
        b = Board()
        assert not b.is_invalid()
        b.fill_space([0,0], 1)
        b.fill_space([0,1], 2)
        b.fill_space([0,2], 3)
        b.fill_space([0,3], 4)
        b.fill_space([0,4], 5)
        b.fill_space([0,5], 6)
        b.fill_space([0,6], 7)
        b.fill_space([0,7], 8)
        b.fill_space([0,8], 9)

        assert not b.is_invalid()
        b.fill_space([0,1], 1)
        assert b.is_invalid()

    def test_is_invalid_with_column(_):
        b = Board()
        assert not b.is_invalid()
        b.fill_space([0,0], 1)
        b.fill_space([1,0], 2)
        b.fill_space([2,0], 3)
        b.fill_space([3,0], 4)
        b.fill_space([4,0], 5)
        b.fill_space([5,0], 6)
        b.fill_space([6,0], 7)
        b.fill_space([7,0], 8)
        b.fill_space([8,0], 9)

        assert not b.is_invalid()
        b.fill_space([1,0], 1)
        assert b.is_invalid()

    def test_is_invalid_with_block(_):
        b = Board()
        assert not b.is_invalid()
        b.fill_space([0,0], 1)
        b.fill_space([0,1], 2)
        b.fill_space([0,2], 3)
        b.fill_space([1,0], 4)
        b.fill_space([1,1], 5)
        b.fill_space([1,2], 6)
        b.fill_space([2,0], 7)
        b.fill_space([2,1], 8)
        b.fill_space([2,2], 9)

        assert not b.is_invalid()
        b.fill_space([0,1], 1)
        assert b.is_invalid()

    def test_to_arr(_):
        b = Board()
        b.fill_space([1,2], 4)
        b.fill_space([1,3], 5)
        board_arr = b.to_arr()
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
