from aoc_utils import aoc_utils
import re

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
      return "Not implemented yet"
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
  
  def find_adjacent_pos(self, pos):
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
  
  def set_distance_map(self):
    self.max_dist = 0
    self.distance_map = [
      [-1 for i in range(self.max_cols)]
      for j in range(self.max_rows)
    ]
    self.distance_map[self.root[0]][self.root[1]] = 0
    explored_pos = [self.root]
    open_pos = self.find_adjacent_pos(self.root)
    open_pos = [p for p in open_pos if self.root in self.find_adjacent_pos(p)]
    steps = 0
    while len(open_pos) > 0:
      steps += 1
      self.max_dist = steps
      explored_pos.extend(open_pos)
      new_pos = []
      for p in open_pos:
        self.distance_map[p[0]][p[1]] = steps
        new_pos.extend(self.find_adjacent_pos(p))
      open_pos = list(set(new_pos) - set(explored_pos))


if __name__ == '__main__':
  day10 = Day10()
  print("Answer for part 1: " + str(day10.solve()))
  print("Answer for part 2: " + str(day10.solve(part = 2)))