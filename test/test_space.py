import sys
sys.path.append("../lib")

import unittest

from space import Space

class SpaceTest(unittest.TestCase):
    def test_possibles(self):
        space = Space()
        self.assertEquals(space.possibles, range(1,10))

    def test_eliminate_possibles(self):
        space = Space()
        space.eliminate_possibles([1,2,3])
        self.assertEquals(space.possibles, range(4,10))
        space.eliminate_possibles(4)
        self.assertEquals(space.possibles, range(5,10))

    def test_intersect_possibles(self):
        space = Space()
        space.intersect_possibles(range(6,10))
        self.assertEquals(space.possibles, range(6,10))
        space.intersect_possibles(range(2,8))
        self.assertEquals(space.possibles, [6,7])

    def test_solve_check(self):
        space = Space()
        space.intersect_possibles(range(6,10))
        space.intersect_possibles(range(3,7))
        self.assertEquals(space.possibles, [6])
        self.assertEquals(space.value, 6)

if __name__ == "__main__":
    unittest.main()
