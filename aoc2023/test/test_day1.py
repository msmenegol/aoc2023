import unittest
from day1 import Day1

class TestDay1(unittest.TestCase):
  test_input = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
  ]
  day1 = Day1()

  def test_solve(self):
    self.assertEqual(
      self.day1.solve(self.test_input),
      142
    )
  
  def test_get_number(self):
    ans = [self.day1.get_number(i) for i in self.test_input]
    self.assertEqual(
      ans,
      ["12", "38", "15", "77"]
    )
  
  def test_fix_input(self):
    test_input = [
      "two1nine",
      "eightwothree",
      "abcone2threexyz",
      "xtwone3four",
      "4nineeightseven2",
      "zoneight234",
      "7pqrstsixteen",
      "1oneightsixsevenine8"
    ]
    ans = self.day1.fix_input(test_input)
    self.assertEqual(
      ans,
      [
        "two2two1nine9nine",
        "eight8eightwo2twothree3three",
        "abcone1one2three3threexyz",
        "xtwo2twone1one3four4four",
        "4nine9nineeight8eightseven7seven2",
        "zone1oneight8eight234",
        '7pqrstsix6sixteen',
        '1one1oneight8eightsix6sixseven7sevenine9nine8'
      ]
    )

if __name__ == '__main__':
    unittest.main()

    