from aoc_utils import aoc_utils
import re
from math import lcm

class Day8(aoc_utils.AoCChallenge):
  day = 8

  def __init__(self):
    super().__init__()
    self.maps = {}
    self.instructions = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    self.set_instructions(input[0])
    self.set_maps(input[2:])
    if part == 2:
      start_positions = self.filter_positions(r'..A')
      end_positions = self.filter_positions(r'..Z')
      steps = [
        self.count_steps(start, end_positions) for start in start_positions
      ]
      ret = 1
      for s in steps:
        ret = lcm(ret, s)
      return ret
    else:
      self.set_instructions(input[0])
      self.set_maps(input[2:])
      return self.count_steps("AAA", ["ZZZ"])
  
  def set_instructions(self, instructions):
    self.instructions = instructions

  def set_maps(self, map_rows):
    map_places = [re.findall(r'[A-Z1-9]{3}', row) for row in map_rows]
    self.maps = {
      places[0]: (places[1], places[2]) for places in map_places 
    }
  
  def count_steps(self, start, end):
    i = 0
    max_i = len(self.instructions)
    place = start
    while not place in end:
      direction = self.instructions[i % max_i]
      if direction == 'R':
        place = self.maps[place][1]
      else:
        place = self.maps[place][0]
      i += 1
    return i
  
  def filter_positions(self, regex):
    return [p for p in self.maps.keys() if re.match(regex, p)]


if __name__ == '__main__':
  day8 = Day8()
  print("Answer for part 1: " + str(day8.solve()))
  print("Answer for part 2: " + str(day8.solve(part = 2)))