import unittest
from day3 import Day3, Number

class TestDay3(unittest.TestCase):
  test_input = [
    "467..114.",
    "...*.....",
    "..35..633",
    "......#..",
    "617*.....",
    ".....+.58",
    "..592....",
    "......755",
    "...$.*...",
    ".664.598."
  ]
  day3 = Day3()
  day3.set_numbers(test_input)

  def test_solve(self):
    self.assertEqual(
      self.day3.solve(self.test_input),
      4361
    )
  
  def test_set_numbers(self):
    self.assertEqual(len(self.day3.numbers), 10)
  
  def test_find_box_content(self):
    content_0 = self.day3.find_box_content(
      self.day3.numbers[0].box,
      self.test_input
    )
    self.assertEqual(content_0, "467....*")

    content_2 = self.day3.find_box_content(
      self.day3.numbers[2].box,
      self.test_input
    )
    self.assertEqual(content_2, "..*..35.....")

    content_3 = self.day3.find_box_content(
      self.day3.numbers[3].box,
      self.test_input
    )
    self.assertEqual(content_3, ".....633.#..")

    content_4 = self.day3.find_box_content(
      self.day3.numbers[4].box,
      self.test_input
    )
    self.assertEqual(content_4, "....617*....")

    content_9 = self.day3.find_box_content(
      self.day3.numbers[9].box,
      self.test_input
    )
    self.assertEqual(content_9, ".*....598.")

class TestNumber(unittest.TestCase):
  def test_init(self):
    number = Number(
      value = 35,
      pos_start = (2, 2),
      pos_end = (2, 3),
      max_row = 9,
      max_column = 8
    )
    self.assertEqual(number.start, (2, 2))
    self.assertEqual(number.end, (2, 3))
    self.assertEqual(number.value, 35)
    self.assertEqual(number.box, ((1, 1), (3, 4)))

  
  def test_calc_box(self):
    number = Number(
      value = 35,
      pos_start = (2, 2),
      pos_end = (2, 3),
      max_row = 9,
      max_column = 3
    )
    self.assertEqual(number.box, ((1, 1), (3, 3)))
    