from aoc_utils import aoc_utils
import re
from math import prod

class Day2(aoc_utils.AoCChallenge):
  day = 2
  max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  games = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if part == 2:
      power_games = [
        game.extract_game_power() for game in self.games
      ]
      return sum(power_games)
    if len(self.games) == 0:
      self.set_games(input)
    possible_games = [
      game.game_id for game in self.games if game.is_game_possible()
    ]
    return sum(possible_games)
  
  def set_games(self, input):
    self.games = [Game(game_text, self.max_cubes) for game_text in input]

class Game():
  def __init__(self, game_text, max_cubes):
    self.max_cubes = max_cubes
    self.colors = list(self.max_cubes.keys())
    self.game_id = int(re.search(r'^Game (\d+): .+', game_text).group(1))
    self.set_trials(game_text)

  def set_trials(self, game_text):
    trials = game_text.split(";")
    self.trials = self.parse_trials_data(trials)    
  
  def parse_trials_data(self, trials):
    trials = [
      {
        color: self.extract_n_cubes(trial, color) for color in self.colors
      }
      for trial in trials
    ]
    return trials

  def extract_n_cubes(self, trial_text, color):
    regex_expr = r' (\d+) ' + color
    n_cubes_match = re.search(regex_expr, trial_text)
    if n_cubes_match == None:
      return 0
    else:
      return int(n_cubes_match.group(1))
  
  def is_game_possible(self):
    for trial in self.trials:
      if not self.is_trial_possible(trial):
        return False
    return True

  def is_trial_possible(self, trial):
    for color in self.colors:
      if trial[color] > self.max_cubes[color]:
        return False
    return True
  
  def extract_game_power(self):
    min_cubes = self.extract_game_min_cubes()
    power = prod(min_cubes.values())
    return power

  def extract_game_min_cubes(self):
    min_cubes = dict(zip(
      self.colors,
      [0] * len(self.colors)
    ))
    for trial in self.trials:
      for color in self.colors:
        if min_cubes[color] < trial[color]:
          min_cubes.update({color: trial[color]})
    return min_cubes 


      




if __name__ == '__main__':
  day2 = Day2()
  print("Answer for part 1: " + str(day2.solve()))
  print("Answer for part 2: " + str(day2.solve(part = 2)))