from aoc_utils import aoc_utils

class Day11(aoc_utils.AoCChallenge):
  day = 11

  def __init__(self):
    super().__init__()
    self.universe = None
  
  def set_universe(self, input):
    self.universe = Universe(input)
    
  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.universe == None:
      self.set_universe(input)
    if part == 2:
      return sum(self.universe.compute_galaxy_distances(1000000))
    else:
      return sum(self.universe.compute_galaxy_distances(2))

class Universe:
  def __init__(self, observation):
    self.uni = observation
    self.empty_rows = self.find_empty_rows(observation)
    self.empty_cols = self.find_empty_cols(observation)
    self.galaxies = self.find_galaxies()

  def find_empty_rows(self, observation):
    empty_rows = []
    for i in range(len(observation)):
      if '#' not in observation[i]:
        empty_rows.append(i)
    return empty_rows

  def find_empty_cols(self, observation):
    t_observation = [list(z) for z in zip(*observation)]
    return self.find_empty_rows(t_observation)
  
  def find_galaxies(self):
    galaxies = []
    for i in range(len(self.uni)):
      for j in range(len(self.uni[0])):
        if self.uni[i][j] == '#':
          galaxies.append((i, j))
    return galaxies

  def compute_galaxy_distances(self, expand_factor = 1):
    distances = []
    for i in range(len(self.galaxies)-1):
      for j in range(i + 1, len(self.galaxies)):
        g1 = self.galaxies[i]
        g2 = self.galaxies[j]
        h_distance = self.find_expanded_distance(
          g1[0],
          g2[0],
          self.empty_rows,
          expand_factor
        )
        v_distance = self.find_expanded_distance(
          g1[1],
          g2[1],
          self.empty_cols,
          expand_factor
        )
        distances.append(h_distance + v_distance)
    return distances
  
  def find_expanded_distance(self, p1, p2, empty_points, expand_factor):
    dist = 0
    high = p2
    low = p1
    if p1 > p2:
      high = p1
      low = p2 
    for p in range(low,high):
      if p in empty_points:
        dist += expand_factor
      else:
        dist += 1
    return dist


if __name__ == '__main__':
  day11 = Day11()
  print("Answer for part 1: " + str(day11.solve()))
  print("Answer for part 2: " + str(day11.solve(part = 2)))

