import unittest
from day6 import Day6

class TestDay5(unittest.TestCase):
  def test_solve(self):
    test_input = """
Time:      7  15   30
Distance:  9  40  200
""".strip('\n').split('\n')
    day6 = Day6()
    self.assertEqual(
      day6.solve(test_input),
      288
    )
  
  def test_solve_part_2(self):
    test_input = """
Time:      7  15   30
Distance:  9  40  200
""".strip('\n').split('\n')
    day6 = Day6()
    self.assertEqual(
      day6.solve(test_input, part = 2),
      71503
    )