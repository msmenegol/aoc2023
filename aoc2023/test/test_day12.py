import unittest
from day12 import Day12

class TestDay12(unittest.TestCase):
  def test_solve(self):
    test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip('\n').split('\n')
    day12 = Day12()
    self.assertEqual(
      day12.solve(test_input),
      21
    )
  
  def test_solve_part_2(self):
    test_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip('\n').split('\n')
    day12 = Day12()
    self.assertEqual(
      day12.solve(test_input, part = 2),
      525152
    )