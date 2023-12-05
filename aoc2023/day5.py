from aoc_utils import aoc_utils
import re

class Day5(aoc_utils.AoCChallenge):
  day = 5

  def __init__(self):
    super().__init__()
    self.maps = {}
    self.starting_seeds = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.starting_seeds == []:
      self.set_starting_seeds(input)
    if self.maps == {}:
      self.set_maps(input)
    if part == 2:    
      return "Not implemented yet"
    else:
      return min(self.find_target_values(self.starting_seeds, "location"))
  
  def set_starting_seeds(self, input):
    tokens = input[0].strip().split()
    self.starting_seeds = [int(s) for s in tokens[1:]]
  
  def set_maps(self, input):
    map_rows = []
    input = input + ['']
    for row in input[1:]:
      if row == '':
        if len(map_rows) > 0:
          _map = Map(map_rows)
          self.maps.update({_map.source: _map})
          map_rows = []
      else:
        map_rows.append(row)
  
  def find_target_values(self, seeds, target_category):
    category = 'seed'
    values = seeds
    while category != target_category:
      _map = self.maps.get(category)
      if _map == None:
        raise(Exception("Map for category "+ category + " does not exist!"))
      values = list(map(_map.find_destination, values))
      category = _map.destination
    return values


class Map:
  def __init__(self, map_rows):
    map_name = map_rows[0]
    [self.source, self.destination] = map_name.rstrip(' map:').split('-to-')
    self._map = []
    for row in map_rows[1:]:
      self.add_row_to_map(row)
   
  def add_row_to_map(self, map_row):
    [dest_range_start, source_range_start, range_length] = [
      int(el) for el in map_row.split()
    ]
    self._map.append(MapRow(dest_range_start, source_range_start, range_length))
  
  def find_destination(self, source_value):
    destination_value = None
    for map_row in self._map:
      destination_value = map_row.find_destination(source_value)
      if destination_value != None:
        return destination_value
    return source_value

class MapRow:
  def __init__(self, dest_start, source_start, length):
    self.dest_start = dest_start
    self.source_start = source_start
    self.source_end = source_start + length - 1
  
  def is_in_source(self, value):
    return value >= self.source_start and value <= self.source_end
  
  def find_destination(self, value):
    if self.is_in_source(value):
      distance = value - self.source_start
      return self.dest_start + distance
    else:
      return None

  




if __name__ == '__main__':
  day5 = Day5()
  print("Answer for part 1: " + str(day5.solve()))
  print("Answer for part 2: " + str(day5.solve(part = 2)))
