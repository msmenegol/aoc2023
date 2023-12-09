from aoc_utils import aoc_utils
import re
from math import lcm

class Day9(aoc_utils.AoCChallenge):
  day = 9

  def __init__(self):
    super().__init__()
    self.report = []
  
  def set_report(self, input):
    self.report = [History(row) for row in input]
    
  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    self.set_report(input)
    if part == 2:
      predictions = [h.predict_backwards() for h in self.report]
      return sum(predictions)
    else:
      predictions = [h.predict_forward() for h in self.report]
      return sum(predictions)


class History:
  def __init__(self, report_row):
    self.readings = [int(val) for val in report_row.split()]
  
  def predict_forward(self):
    return self.predict_next(self.readings)

  def predict_backwards(self):
    return self.predict_previous(self.readings)

  def predict_next(self, seq):
    if len(set(seq)) == 1:
      return seq[-1]
    else:
      step_seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
      return self.predict_next(step_seq) + seq[-1]
  
  def predict_previous(self, seq):
    if len(set(seq)) == 1:
      return seq[0]
    else:
      step_seq = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
      return seq[0] - self.predict_previous(step_seq) 
     

if __name__ == '__main__':
  day9 = Day9()
  print("Answer for part 1: " + str(day9.solve()))
  print("Answer for part 2: " + str(day9.solve(part = 2)))