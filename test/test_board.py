import sys
sys.path.append("../lib")

import unittest

from board import Board
from space import Space

class BoardTest(unittest.TestCase):
    def test_get_vert_spaces(self):
        b = Board(4)
        vert_spaces = [
            [0,2],
            [1,2],
            [2,2],
            [3,2]
        ]
        self.assertEquals(b.get_vert_spaces([1,2]), vert_spaces)

    def test_get_hor_spaces(self):
        b = Board(4)
        hor_spaces = [
            [1,0],
            [1,1],
            [1,2],
            [1,3],
        ]
        self.assertEquals(b.get_hor_spaces([1,2]), hor_spaces)

    def test_get_block_spaces(self):
        b = Board()
        block_spaces = [
            [0,6],[0,7],[0,8],
            [1,6],[1,7],[1,8],
            [2,6],[2,7],[2,8]
        ]
        self.assertEquals(b.get_block_spaces([1,7]), block_spaces)
    def test_get_eliminating_values(self):
        b = Board()
        b.fill_space([1,2],5)
        b.fill_space([1,1],4)
        eliminating_values = [4,5]
        self.assertEquals(b.get_eliminating_values([1,3]), eliminating_values)

if __name__ == "__main__":
    unittest.main()
