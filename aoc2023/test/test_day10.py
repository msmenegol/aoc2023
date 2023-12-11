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
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip('\n').split('\n')
    day10 = Day10()
    self.assertEqual(
      day10.solve(test_input, part = 2),
      10
    )