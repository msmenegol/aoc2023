from aoc_utils import aoc_utils
import re

class Day4(aoc_utils.AoCChallenge):
  day = 4
  scratchcards = {}

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if self.scratchcards == {}:
        self.set_scratchcards(input)
    if part == 2:
      self.update_scratchcard_intances()
      n_cards = [sc.instances for sc in self.scratchcards.values()]      
      return sum(n_cards)
    else:
      points = [sc.calc_points() for sc in self.scratchcards.values()]
      return sum(points)
  
  def set_scratchcards(self, input):
    scratchcards = [Scratchcard(row) for row in input]
    card_ids = [sc.card_id for sc in scratchcards]
    self.scratchcards = dict(zip(card_ids, scratchcards))
  
  def update_scratchcard_intances(self):
    for k in self.scratchcards.keys():
      sc = self.scratchcards[k]
      n_matches = sc.calc_n_matches()
      instances = sc.instances
      if n_matches > 0:
        card_ids_to_update = range(sc.card_id + 1, sc.card_id + n_matches + 1)
        for card_id in card_ids_to_update:
          self.scratchcards[card_id].add_instances(instances)


class Scratchcard():
  def __init__(self, card_text):
    card_parts = card_text.replace(':', '|').split('|')
    self.instances = 1
    self.card_id = int(re.search(r'\d+', card_parts[0])[0])
    self.winning_numbers = [int(n) for n in card_parts[1].strip().split()]
    self.numbers = [int(n) for n in card_parts[2].strip().split()] 
  
  def calc_points(self):
    n_matches = self.calc_n_matches()
    points = pow(2, n_matches - 1) if n_matches > 0 else 0
    return points
  
  def calc_n_matches(self):
    matching_numbers = set(self.winning_numbers).intersection(self.numbers)
    return len(matching_numbers)
  
  def add_instances(self, n):
    self.instances += n


if __name__ == '__main__':
  day4 = Day4()
  print("Answer for part 1: " + str(day4.solve()))
  print("Answer for part 2: " + str(day4.solve(part = 2)))
