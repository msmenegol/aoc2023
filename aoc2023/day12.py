from aoc_utils import aoc_utils

class Day12(aoc_utils.AoCChallenge):
  day = 12

  def __init__(self):
    super().__init__()
    self.records = []
  
  def set_records(self, input, instances = 1):
    self.records = [Record(row, instances) for row in input]
    
  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.records == []:
      self.set_records(input)
    if part == 2:
      self.set_records(input, instances = 5)
      return sum([r.find_combinations() for r in self.records])
    else:
      self.set_records(input)
      return sum([r.find_combinations() for r in self.records])


class Record:
  def __init__(self, record_row, instances = 1):
    springs, dmg_outcome = record_row.split()
    self.springs = '?'.join([springs] * instances)
    dmg_outcome  = ','.join([dmg_outcome] * instances)
    self.damage_outcome = [int(d) for d in dmg_outcome.split(',')]
    self.damaged_groups = [g for g in self.springs.split('.') if g != '']
    self.simplified_springs = '.'.join(self.damaged_groups)
    self.combinations = {}
  
  def find_combinations(self):
    return self.find_combinations_from(0, 0, 0)

  def find_combinations_from(self, si, gi, gs):
    key = (si, gi, gs)
    if key in self.combinations:
      return self.combinations[key]
    springs = self.simplified_springs
    outcomes = self.damage_outcome
    if si == len(springs):
      if gi == len(outcomes) and gs == 0:
        return 1
      elif gi == len(outcomes) - 1 and outcomes[gi] == gs:
        return 1 
      else:
        return 0
    comb = 0
    for c in ['#', '.']:
      if springs[si] == c or springs[si] == '?':
        if c == '.' and gs == 0:
          comb += self.find_combinations_from(si+1, gi, 0)
        elif c == '.' and gs > 0 and gi < len(outcomes) and outcomes[gi] == gs:
          comb += self.find_combinations_from(si+1, gi+1, 0)
        elif c == '#':
          comb += self.find_combinations_from(si+1, gi, gs+1)
    self.combinations.update({key: comb})
    return comb


if __name__ == '__main__':
  day12 = Day12()
  print("Answer for part 1: " + str(day12.solve()))
  print("Answer for part 2: " + str(day12.solve(part = 2)))




