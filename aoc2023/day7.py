from aoc_utils import aoc_utils

class Day7(aoc_utils.AoCChallenge):
  day = 7

  def __init__(self):
    super().__init__()
    self.hands = []

  def solve(self, input = None, part = 1):
    if input == None:
      input = self.input
    if part == 2:
      card_order = [
        'A',
        'K',
        'Q',
        'T',
        '9',
        '8',
        '7',
        '6',
        '5',
        '4',
        '3',
        '2',
        'J'
      ][::-1]
      self.set_hands(input, card_order, joker = 'J')
      self.sort_hands()
      return self.calculate_total_winnings()
    else:
      card_order = [
        'A',
        'K',
        'Q',
        'J',
        'T',
        '9',
        '8',
        '7',
        '6',
        '5',
        '4',
        '3',
        '2'
      ][::-1]
      self.set_hands(input, card_order)
      self.sort_hands()
      return self.calculate_total_winnings()
  
  def set_hands(self, input, card_order, joker = None):
    self.hands = [Hand(row, card_order, joker = joker) for row in input]

  def sort_hands(self):
    self.hands = sorted(self.hands, key = Hand.calculate_strength)
  
  def calculate_total_winnings(self):
    winnings = [self.hands[i].bid * (i + 1) for i in range(len(self.hands))]
    return sum(winnings)


class Hand:
  def __init__(self, input_row, card_order, joker = None):
    self.card_order = card_order
    self.joker = joker
    cards, bid = input_row.split()
    self.cards = cards
    self.bid = int(bid)
    self.set_hand_type()
  
  def set_hand_type(self):
    card_count_dict = {c: self.cards.count(c) for c in self.card_order}
    if self.joker != None:
      card_count_dict = self.add_joker_to_card_count(card_count_dict)
    card_count = list(card_count_dict.values())
    if 5 in card_count:
      self.hand_type = 6
    elif 4 in card_count:
      self.hand_type = 5
    elif 3 in card_count:
      if 2 in card_count:
        self.hand_type = 4
      else:
        self.hand_type = 3
    elif 2 in card_count:
      if card_count.count(2) > 1:
        self.hand_type = 2
      else:
        self.hand_type = 1
    else:
      self.hand_type = 0
  
  def add_joker_to_card_count(self, card_count_dict):
    joker_count = card_count_dict[self.joker]
    card_count_dict[self.joker] = 0
    max_count_card = max(card_count_dict, key = card_count_dict.get)
    if card_count_dict[max_count_card] == 0:
      max_count_card = self.card_order[-1]
    card_count_dict[max_count_card] += joker_count
    return card_count_dict


  @classmethod
  def calculate_strength(cls, hand):
    hex_cards_strength = [
      hex(hand.card_order.index(card)).replace('0x', '')
      for card in hand.cards
    ]
    hex_hand_strength = '0x' + ''.join(
      [str(hand.hand_type)] + hex_cards_strength
    )
    return int(hex_hand_strength, 16)


if __name__ == '__main__':
  day7 = Day7()
  print("Answer for part 1: " + str(day7.solve()))
  print("Answer for part 2: " + str(day7.solve(part = 2)))

  
