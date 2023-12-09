import unittest
from day9 import Day9

class TestDay8(unittest.TestCase):
  def test_solve(self):
    test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip('\n').split('\n')
    day9 = Day9()
    self.assertEqual(
      day9.solve(test_input),
      114
    )
  
  def test_solve_part_2(self):
    test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip('\n').split('\n')
    day9 = Day9()
    self.assertEqual(
      day9.solve(test_input, part = 2),
      2
    )