import sys
sys.path.append("../lib")

import unittest

from space import Space

class SpaceTest(unittest.TestCase):
    def test_possibles(_):
        space = Space()
        _.assertEquals(space.possibles, range(1,10))

    def test_eliminate_possibles(_):
        space = Space()
        space.eliminate_possibles([1,2,3])
        _.assertEquals(space.possibles, range(4,10))
        space.eliminate_possibles(4)
        _.assertEquals(space.possibles, range(5,10))

    def test_intersect_possibles(_):
        space = Space()
        space.intersect_possibles(range(6,10))
        _.assertEquals(space.possibles, range(6,10))
        space.intersect_possibles(range(2,8))
        _.assertEquals(space.possibles, [6,7])

    def test_solve_check(_):
        space = Space()
        space.intersect_possibles(range(6,10))
        space.intersect_possibles(range(3,7))
        _.assertEquals(space.possibles, [6])
        _.assertEquals(space.value, 6)

if __name__ == "__main__":
    unittest.main()
