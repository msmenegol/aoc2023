from aoc_utils import aoc_utils
from math import ceil, floor, sqrt, prod

class Day6(aoc_utils.AoCChallenge):
  day = 6

  def __init__(self):
    super().__init__()
    self.races = []
    self.records = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.races == []:
      self.set_races(input)
    if self.records == []:
      self.set_records(input)
    if part == 2:
      race_time = int(''.join([t for t in input[0].split()[1:]]))
      record = int(''.join([d for d in input[1].split()[1:]]))
      race = Race(race_time)
      return race.find_n_holds_for_record(record)
    else:
      n_hold_times = [
        self.races[i].find_n_holds_for_record(self.records[i])
        for i in range(len(self.races))
      ]
      return prod(n_hold_times)
  
  def set_races(self, input):
    self.races = [Race(int(t)) for t in input[0].split()[1:]]
  
  def set_records(self, input):
    self.records = [int(d) for d in input[1].split()[1:]]
  


class Race:
  def __init__(self, time):
    self.time = time
  
  def find_n_holds_for_record(self, record):
    (min_time, max_time) = self.find_min_max_times_for_record(record)
    if min_time == None or max_time == None:
      return 0
    else: 
      return max_time - min_time + 1
  
  def find_min_max_times_for_record(self, record):
    return self.solve_neg_int_quad_eq(
      -1,
      self.time,
      -record
    )
  
  def solve_neg_int_quad_eq(self, a, b, c):
    if a >= 0:
      raise(Exception("a is not negative"))
    delta = pow(b,2) - 4 * a * c
    if delta < 0:
      return (None, None)
    else:
      x_max = (b + sqrt(delta)) / 2
      x_max = int(ceil(x_max - 1))
      x_min = (b - sqrt(delta)) / 2
      x_min = int(floor(x_min + 1))
      return (x_min, x_max)


if __name__ == '__main__':
  day6 = Day6()
  print("Answer for part 1: " + str(day6.solve()))
  print("Answer for part 2: " + str(day6.solve(part = 2)))