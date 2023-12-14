import unittest
from day13 import Day13

class TestDay13(unittest.TestCase):
  def test_solve(self):
    test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip('\n').split('\n')
    day13 = Day13()
    self.assertEqual(
      day13.solve(test_input),
      405
    )
  
  def test_solve_part_2(self):
    test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip('\n').split('\n')
    day13 = Day13()
    self.assertEqual(
      day13.solve(test_input, part = 2),
      401
    )