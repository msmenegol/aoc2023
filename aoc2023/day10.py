from aoc_utils import aoc_utils

class Day10(aoc_utils.AoCChallenge):
  day = 10

  def __init__(self):
    super().__init__()
    self.maze = None
  
  def set_maze(self, input):
    self.maze = Maze(input)
    
  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.maze == None:
      self.set_maze(input)
    if part == 2:
      return self.maze.count_inside_areas()
    else:
      return self.maze.max_dist

class Maze:
  def __init__(self, maze_map):
    self.maze_map = maze_map
    self.max_rows = len(self.maze_map)
    self.max_cols = len(self.maze_map[0])
    self.set_root()
    self.set_distance_map()

  def set_root(self):
    self.root = None
    for i in range(self.max_rows):
      for j in range(self.max_cols):
        if self.maze_map[i][j] == 'S':
          self.root = (i, j)
    if self.root == None:
      raise(Exception('COULD NOT FIND ROOT'))
  
  def find_adjacent_tiles(self, pos):
    north = (max(pos[0] - 1, 0), pos[1])
    east = (pos[0], min(pos[1] + 1, self.max_cols))
    west = (pos[0], max(pos[1] - 1, 0))
    south = (min(pos[0] + 1, self.max_rows), pos[1])
    token = self.maze_map[pos[0]][pos[1]]
    adjacent_pos = set()
    if token == 'S':
      adjacent_pos = set([north, east, west, south])
    if token == '|':
      adjacent_pos = set([north, south])
    if token == '-':
      adjacent_pos = set([east, west])
    if token == 'J':
      adjacent_pos = set([west, north])
    if token == 'L':
      adjacent_pos = set([east, north])
    if token == 'F':
      adjacent_pos = set([east, south])
    if token == '7':
      adjacent_pos = set([west, south])
    if token == '.':
      adjacent_pos = set()
    adjacent_pos = adjacent_pos - set([pos])
    return list(adjacent_pos)
  
  def find_adjacent_pos(self, pos):
    north = (max(pos[0] - 1, 0), pos[1])
    east = (pos[0], min(pos[1] + 1, self.max_cols))
    west = (pos[0], max(pos[1] - 1, 0))
    south = (min(pos[0] + 1, self.max_rows), pos[1])
    adjacent = set([north, east, west, south]) - set([pos])
    return list(adjacent)
  
  def set_distance_map(self):
    self.max_dist = 0
    self.distance_map = [
      [-1 for i in range(self.max_cols)]
      for j in range(self.max_rows)
    ]
    self.distance_map[self.root[0]][self.root[1]] = 0
    self.loop_points = [self.root]
    explored_pos = [self.root]
    open_pos = self.find_adjacent_tiles(self.root)
    open_pos = [p for p in open_pos if self.root in self.find_adjacent_tiles(p)]
    steps = 0
    while len(open_pos) > 0:
      steps += 1
      self.max_dist = steps
      explored_pos.extend(open_pos)
      new_pos = []
      for p in open_pos:
        self.distance_map[p[0]][p[1]] = steps
        new_pos.extend(self.find_adjacent_tiles(p))
        self.loop_points.append(p)
      open_pos = list(set(new_pos) - set(explored_pos))
  
  def count_inside_areas(self):
    areas = self.find_areas()
    regions = self.categorize_areas(areas)
    return sum([len(area) for area in regions['in']])
  
  def find_areas(self):
    points = [
      (i, j)
      for i in range(self.max_rows)
      for j in range(self.max_cols)
    ]
    points = set([p for p in points if p not in self.loop_points])
    areas = []
    open_points = []
    while len(points) > 0:
      if open_points == []:
        open_points.append(points.pop())
      point = open_points.pop()
      adjacents = self.find_adjacent_pos(point)
      is_free = True
      for i in range(len(areas)):
        area = areas[i]
        is_in_area = [a in area for a in adjacents]
        if any(is_in_area):
          areas[i] = area + [point]
          is_free = False
      if is_free:
        areas.append([point])
      free_adjacents = [
        a for a in adjacents
        if a not in open_points and a in points
      ]
      open_points.extend(free_adjacents)
      points = points - set(free_adjacents + [point])
    return areas
  
  def categorize_areas(self, areas):
    inside = []
    outside = []
    for area in areas:
      p = area[0]
      loop_crosses = self.find_loop_crosses(p)
      if loop_crosses % 2 == 1:
        inside.append(area)
      else:
        outside.append(area)
    return {
      'in': inside,
      'out': outside
    }
  
  def find_loop_crosses(self, point):
    row_points = [(point[0], j) for j in range(point[1])]
    tokens = [self.maze_map[rp[0]][rp[1]] for rp in row_points]
    if 'S' in tokens:
      s_idx = tokens.index('S')
      tokens[s_idx] = self.replace_root_token()
    crosses = ''.join([
      tokens[i] for i in range(point[1])
      if row_points[i] in self.loop_points and not tokens[i] == '-'
    ])
    crosses = crosses.replace('FJ', '|').replace('L7','|')
    return len(crosses)
  
  def replace_root_token(self):
    north = (max(self.root[0] - 1, 0), self.root[1])
    north_token = self.maze_map[north[0]][north[1]]
    east = (self.root[0], min(self.root[1] + 1, self.max_cols))
    east_token = self.maze_map[east[0]][east[1]]
    west = (self.root[0], max(self.root[1] - 1, 0))
    west_token = self.maze_map[west[0]][west[1]]
    south = (min(self.root[0] + 1, self.max_rows), self.root[1])
    south_token = self.maze_map[south[0]][south[1]]
    if north_token in ['7','|','F'] and south_token in ['J', '|', 'L']:
      return '|'
    elif north_token in ['7','|','F'] and east_token in ['7', '-', 'J']:
      return 'L'
    elif north_token in ['7','|','F'] and west_token in ['L', '-', 'F']:
      return 'J'
    elif west_token in ['L','-','F'] and east_token in ['J', '-', '7']:
      return '-'
    elif west_token in ['L','-','F'] and south_token in ['J', '|', 'L']:
      return '7'
    elif south_token in ['J','|','L'] and east_token in ['J', '-', '7']:
      return 'F'
    raise(Exception('COULD NOT REPLACE ROOT'))


if __name__ == '__main__':
  day10 = Day10()
  print("Answer for part 1: " + str(day10.solve()))
  print("Answer for part 2: " + str(day10.solve(part = 2)))