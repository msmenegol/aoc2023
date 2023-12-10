import unittest
from day10 import Day10

class TestDay10(unittest.TestCase):
  def test_solve(self):
    test_input = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip('\n').split('\n')
    day10 = Day10()
    self.assertEqual(
      day10.solve(test_input),
      8
    )
  
  def test_solve_part_2(self):
    test_input = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""".strip('\n').split('\n')
    day10 = Day10()
    self.assertEqual(
      day10.solve(test_input, part = 2),
      "Not implemented yet"
    )