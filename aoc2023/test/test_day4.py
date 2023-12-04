import unittest
from day4 import Day4, Scratchcard

class TestDay3(unittest.TestCase):
  test_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
  ]
  day4 = Day4()

  def test_solve(self):
    self.assertEqual(
      self.day4.solve(self.test_input),
      13
    )
  
  def test_solve_part_2(self):
    self.assertEqual(
      self.day4.solve(self.test_input, part = 2),
      30
    )

class TestScratchcard(unittest.TestCase):
  test_input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
  sc = Scratchcard(test_input)

  def test_init(self):
    self.assertEqual(self.sc.card_id, 1)
    self.assertEqual(
      self.sc.numbers,
      [83, 86, 6, 31, 17, 9, 48, 53]
    )
    self.assertEqual(
      self.sc.winning_numbers,
      [41, 48, 83, 86, 17]
    )
  
  def test_calc_points(self):
    self.assertEqual(
      self.sc.calc_points(),
      8
    )