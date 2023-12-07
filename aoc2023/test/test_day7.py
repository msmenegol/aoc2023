import unittest
from day7 import Day7, Hand

class TestDay7(unittest.TestCase):
  def test_solve(self):
    test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip('\n').split('\n')
    day7 = Day7()
    self.assertEqual(
      day7.solve(test_input),
      6440
    )
  
  def test_solve_part_2(self):
    test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip('\n').split('\n')
    day7 = Day7()
    self.assertEqual(
      day7.solve(test_input, part = 2),
      5905
    )