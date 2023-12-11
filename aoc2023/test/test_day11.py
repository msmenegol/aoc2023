import unittest
from day11 import Day11

class TestDay11(unittest.TestCase):
  def test_solve(self):
    test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip('\n').split('\n')
    day11 = Day11()
    self.assertEqual(
      day11.solve(test_input),
      374
    )
  
  def test_solve_part_2(self):
    test_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip('\n').split('\n')
    day11 = Day11()
    self.assertEqual(
      day11.solve(test_input, part = 2),
      82000210
    )