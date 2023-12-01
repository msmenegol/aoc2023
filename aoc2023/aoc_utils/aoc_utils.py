class AoCChallenge:
  input = ""
  day = 0

  def __init__(self):
    self.input_path = "/usr/src/aoc2023/inputs/day" + str(self.day) + ".txt"
    self.load_input()
    
  def load_input(self):
    with open(self.input_path) as f:
      self.input = f.readlines()
  
  def get_input(self):
    if self.input == "":
      self.load_input()
    return self.input
  
  def solve(self, input):
    pass