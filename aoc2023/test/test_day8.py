import unittest
from day8 import Day8

class TestDay8(unittest.TestCase):
  def test_solve(self):
    test_input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip('\n').split('\n')
    day8 = Day8()
    self.assertEqual(
      day8.solve(test_input),
      6
    )
  
  def test_solve_part_2(self):
    test_input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip('\n').split('\n')
    day8 = Day8()
    self.assertEqual(
      day8.solve(test_input, part = 2),
      6
    )