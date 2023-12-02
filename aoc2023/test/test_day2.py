import unittest
from day2 import Day2, Game

class TestDay2(unittest.TestCase):
  test_input = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
  ]
  day2 = Day2()

  def test_solve(self):
    self.assertEqual(
      self.day2.solve(self.test_input),
      8
    )
  
  def test_set_games(self):
    self.day2.set_games(self.test_input)
    self.assertEqual(
      len(self.day2.games),
      5
    )

class TestGame(unittest.TestCase):
  test_input = \
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
  max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  game = Game(test_input, max_cubes)

  def test_init(self):
    self.assertEqual(
      self.game.game_id,
      3
    )
    self.assertEqual(
      self.game.max_cubes,
      self.max_cubes
    )
    self.assertEqual(
      self.game.colors,
      list(self.max_cubes.keys())
    )
    self.assertEqual(
      self.game.trials[0],
      {
        "red": 20,
        "green": 8,
        "blue": 6
      }
    )
    self.assertEqual(
      self.game.trials[2],
      {
        "red": 1,
        "green": 5,
        "blue": 0
      }
    )
  
  def test_is_trial_possible(self):
    self.assertFalse(
      self.game.is_trial_possible(self.game.trials[0])
    )
    self.assertTrue(
      self.game.is_trial_possible(self.game.trials[2])
    )

  def test_is_game_possible(self):
    self.assertFalse(
      self.game.is_game_possible()
    )
    

if __name__ == '__main__':
    unittest.main()