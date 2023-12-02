from aoc_utils import aoc_utils

class Day1(aoc_utils.AoCChallenge):
  day = 1
  number_map = list(zip(
    ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
    [str(i+1) for i in range(9)]
  ))

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if part == 2:
      input = self.fix_input(input)
    numbers = [int(self.get_number(i)) for i in input]
    ans = sum(numbers)
    return(ans)

  def get_number(self, input_element):
    number = self.get_first(input_element) + self.get_last(input_element)
    return(number)

  def get_first(self, input_element):
    for i in input_element:
      if i.isnumeric():
        return(i)

  def get_last(self, input_element):
    for i in input_element[::-1]:
      if i.isnumeric():
        return(i)
  
  def fix_input(self, input):
    fixed_input = [self.replace_text_num(i) for i in input]
    return(fixed_input)
  
  def replace_text_num(self, text):
    for i in range(len(self.number_map)):
      num_as_text = self.number_map[i][0]
      num_as_num = self.number_map[i][1]
      text = text.replace(num_as_text, num_as_text + num_as_num + num_as_text)
    return(text)


if __name__ == '__main__':
  day1 = Day1()
  print("Answer for part 1: " + str(day1.solve()))
  print("Answer for part 2: " + str(day1.solve(part = 2)))
  