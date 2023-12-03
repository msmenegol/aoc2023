from aoc_utils import aoc_utils
import re

class Day3(aoc_utils.AoCChallenge):
  day = 3
  numbers = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if part == 2:
      return("Not implemented yet")
    valid_numbers = self.find_valid_numbers(input)
    return sum(valid_numbers)
  
  def find_valid_numbers(self, input):
    valid_numbers = []
    if self.numbers == []:
      self.set_numbers(input)
    for num in self.numbers:
      content = self.find_box_content(num.box, input)
      if self.is_content_valid(content):
        valid_numbers.append(num.value)
    return valid_numbers
  
  def set_numbers(self, input):
    numbers = []
    self.max_row = len(input) - 1
    self.max_column = len(input[0]) - 1
    for row_idx in range(len(input)):
      row = input[row_idx]
      for match in re.finditer(r'\d+', row):
        number = Number(
          value = int(match[0]),
          pos_start = (row_idx, match.span()[0]),
          pos_end = (row_idx, match.span()[1]-1),
          max_row = self.max_row,
          max_column = self.max_column
        )
        numbers.append(number)
    self.numbers = numbers
    
  
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
    


class Number():
  def __init__(self, value, pos_start, pos_end, max_row, max_column):
    self.start = pos_start
    self.end = pos_end
    self.value = int(value)
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


