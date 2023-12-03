from aoc_utils import aoc_utils
import re
from math import prod

class Day3(aoc_utils.AoCChallenge):
  day = 3
  numbers = []
  valid_numbers = []
  gears = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if part == 2:
      gear_ratios = self.find_gear_ratios(input)
      return sum(gear_ratios)
    else:
      if self.valid_numbers == []:
        self.set_valid_numbers(input)
      valid_number_values = [num.value for  num in self.valid_numbers]
      return sum(valid_number_values)

  def find_gear_ratios(self, input):
    gear_ratios = []
    if self.gears == []:
      self.set_gears(input)
    if self.valid_numbers == []:
      self.set_valid_numbers(input)
    for gear in self.gears:
      gear_ratio = self.find_gear_ratio(gear, self.valid_numbers)
      gear_ratios.append(gear_ratio)
    return gear_ratios

  def find_gear_ratio(self, gear, numbers):
    intercepting_numbers = self.find_intercepting_numbers(gear.box, numbers)
    if len(intercepting_numbers) > 2:
      raise(Exception(
        "GEAR WITH MORE THAN 2 NUMBERS. BOX = " + str(gear.box)
      ))
    elif len(intercepting_numbers) < 2:
      return 0
    else:
      return prod(intercepting_numbers)
  
  def find_intercepting_numbers(self, box, numbers):
    intercepting_numbers = []
    for num in numbers:
      if num.intercepts(box):
        intercepting_numbers.append(num.value)
    return intercepting_numbers

  def set_valid_numbers(self, input):
    valid_numbers = []
    if self.numbers == []:
      self.set_numbers(input)
    for num in self.numbers:
      content = self.find_box_content(num.box, input)
      if self.is_content_valid(content):
        valid_numbers.append(num)
    self.valid_numbers = valid_numbers
  
  def set_numbers(self, input):
    self.numbers = self.find_tokens(input, r'\d+', is_number = True)
  
  def set_gears(self, input):
    self.gears = self.find_tokens(input, r'\*')
  
  def find_tokens(self, input, regex, is_number = False):
    tokens = []
    self.max_row = len(input) - 1
    self.max_column = len(input[0]) - 1
    for row_idx in range(len(input)):
      row = input[row_idx]
      for match in re.finditer(regex, row):
        if is_number:
          number = Number(
            value = int(match[0]),
            pos_start = (row_idx, match.span()[0]),
            pos_end = (row_idx, match.span()[1]-1),
            max_row = self.max_row,
            max_column = self.max_column
          )
          tokens.append(number)
        else:
          token = Token(
            pos_start = (row_idx, match.span()[0]),
            pos_end = (row_idx, match.span()[1]-1),
            max_row = self.max_row,
            max_column = self.max_column
          )
          tokens.append(token)
    return tokens


  
  def find_box_content(self, box, input):
    box_start = box[0]
    box_end = box[1]
    content = [
      row[box_start[1]:box_end[1]+1]
      for row in input[box_start[0]:box_end[0]+1]
    ]
    content = ''.join(content)
    return(content)
  
  def is_content_valid(self, content):
    return(re.search(r'[^\d|\.]', content) != None)
    

class Token():
  def __init__(self, pos_start, pos_end, max_row, max_column):
    self.start = pos_start
    self.end = pos_end
    self.box = self.calc_box(self.start, self.end, max_row, max_column)

  def calc_box(self, start, end, max_row, max_column):
    box_start = (
      max(start[0]-1, 0),
      max(start[1]-1, 0)
    )
    box_end = (
      min(end[0]+1, max_row),
      min(end[1]+1, max_column)
    )
    return((box_start, box_end))

  def intercepts(self, box):
    box_start = box[0]
    box_end = box[1]
    is_number_outside_box = \
      self.end[0] < box_start[0] \
      or self.start[0] > box_end[0] \
      or self.end[1] < box_start[1] \
      or self.start[1] > box_end[1]
    return not is_number_outside_box
  
  def __repr__(self):
    return f"""<
  Token:
    start: {self.start},
    end: {self.end},
    box: {self.box}
>"""

class Number(Token):
  def __init__(self, value, pos_start, pos_end, max_row, max_column):
    super().__init__(pos_start, pos_end, max_row, max_column)
    self.value = int(value)

  def __repr__(self):
    return f"""<
  Number:
    value: {self.value},
    start: {self.start},
    end: {self.end},
    box: {self.box}
>"""

if __name__ == '__main__':
  day3 = Day3()
  print("Answer for part 1: " + str(day3.solve()))
  print("Answer for part 2: " + str(day3.solve(part = 2)))


