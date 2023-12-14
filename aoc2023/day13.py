from aoc_utils import aoc_utils


class Day13(aoc_utils.AoCChallenge):
  day = 13

  def __init__(self):
    super().__init__()
    self.patterns = []
    
  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.patterns == []:
      self.set_patterns(input)
    if part == 2:
      return sum([
        p.find_pattern_score(consider_smudge = True)
        for p in self.patterns
      ])
    else:
      return sum([p.find_pattern_score() for p in self.patterns])

  def set_patterns(self, input):
    pattern = []
    for row in input:
      if row == '':
        self.patterns.append(Pattern(pattern))
        pattern = []
      else:
        pattern.append(row)
    self.patterns.append(Pattern(pattern))


class Pattern:
  def __init__(self, pattern):
    self.pattern = pattern
    self.cleaned_smudge = False
  
  def find_pattern_score(self, consider_smudge = False):
    score = 0
    score += self.find_horizontal_score(self.pattern, consider_smudge)
    score += self.find_vertical_score(self.pattern, consider_smudge)
    return score
  
  def find_horizontal_score(self, pattern, consider_smudge):
    old_pattern = pattern
    rows_match_map = {}
    cleaned_smudge = False
    for i in range(len(pattern) - 1):
      half_window_size = min(i + 1, len(pattern) - i - 1)
      is_symetrical = True
      for j in range(half_window_size):
        ui = i - half_window_size + j + 1
        li = i + half_window_size - j
        key = (ui,li)
        rows_match = False
        if key in rows_match_map:
          rows_match = rows_match_map[key]
        else:
          rows_match = pattern[ui] == pattern[li]
          rows_match_map[key] = rows_match
        if not rows_match:
          if consider_smudge:
            if not cleaned_smudge:
              diffs = [
                pattern[ui][k] != pattern[li][k]
                for k in range(len(pattern[0]))
              ]
              if sum(diffs) == 1:
                smudge_pos = (ui, diffs.index(True))
                pattern = self.clean_smudge(smudge_pos, pattern)
                rows_match = True
                cleaned_smudge = True
            else:
              is_symetrical = False
              pattern = old_pattern
              cleaned_smudge = False
          else:
            is_symetrical = False
      if is_symetrical:
        if consider_smudge:
          if cleaned_smudge:
            return 100 * (i + 1)
        else:
          return 100 * (i + 1)
    return 0
  
  def find_vertical_score(self, pattern, consider_smudge):
    t_pattern = [''.join(z) for z in zip(*pattern)]
    score = self.find_horizontal_score(t_pattern, consider_smudge)
    return score // 100
  
  def clean_smudge(self, smudge_pos, pattern):
    smudge = pattern[smudge_pos[0]][smudge_pos[1]]
    if smudge == '.':
      pattern[smudge_pos[0]] = \
        pattern[smudge_pos[0]][:smudge_pos[1]] \
        + '#' \
        + pattern[smudge_pos[0]][smudge_pos[1]+1:]
    else:
      pattern[smudge_pos[0]] = \
        pattern[smudge_pos[0]][:smudge_pos[1]] \
        + '.' \
        + pattern[smudge_pos[0]][smudge_pos[1]+1:]
    return pattern


if __name__ == '__main__':
  day13 = Day13()
  print("Answer for part 1: " + str(day13.solve()))
  print("Answer for part 2: " + str(day13.solve(part = 2)))