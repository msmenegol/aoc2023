import unittest
from day5 import Day5, Map, MapRow

class TestDay5(unittest.TestCase):
  def test_find_target_values(self):
    test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15""".strip('\n').split('\n')
    day5 = Day5()
    day5.set_starting_seeds(test_input)
    day5.set_maps(test_input)
    self.assertEqual(
      day5.find_target_values([99, 60, 10], "soil"),
      [51, 62, 10]
    )
    self.assertEqual(
      day5.find_target_values([1000], "fertilizer"),
      [1000]
    )

  def test_solve(self):
    test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip('\n').split('\n')
    day5 = Day5()
    self.assertEqual(
      day5.solve(test_input),
      35
    )
  
  def test_solve_part_2(self):
    test_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".strip('\n').split('\n')
    day5 = Day5()
    self.assertEqual(
      day5.solve(test_input, part = 2),
      46
    )


class TestMap(unittest.TestCase):
  def test_init(self):
    test_input = \
"""
seed-to-soil map:
50 98 2
52 50 48""".strip('\n').split('\n')
    _map = Map(test_input)
    self.assertEqual(_map.source, "seed")
    self.assertEqual(_map.destination, "soil")
    self.assertEqual(len(_map._map), 2)
  
  def test_find_destination(self):
    test_input = \
"""
seed-to-soil map:
50 98 2
52 50 48""".strip('\n').split('\n')
    _map = Map(test_input)
    self.assertEqual(
      _map.find_destination(98),
      50
    )
    self.assertEqual(
      _map.find_destination(99),
      51
    )
    self.assertEqual(
      _map.find_destination(60),
      62
    )
    self.assertEqual(
      _map.find_destination(10),
      10
    )

class TestMapRow(unittest.TestCase):
  def test_init(self):
    map_row = MapRow(52, 50, 48)
    self.assertEqual(map_row.dest_start, 52)
    self.assertEqual(map_row.source_start, 50)
    self.assertEqual(map_row.source_end, 97)
  
  def test_is_in_source(self):
    map_row = MapRow(52, 50, 48)
    self.assertTrue(map_row.is_in_source(50))
    self.assertTrue(map_row.is_in_source(97))
    self.assertTrue(map_row.is_in_source(60))
    self.assertFalse(map_row.is_in_source(98))
    self.assertFalse(map_row.is_in_source(100))
    self.assertFalse(map_row.is_in_source(49))
    self.assertFalse(map_row.is_in_source(10))
  
  def test_find_destination(self):
    map_row = MapRow(52, 50, 48)
    self.assertEqual(
      map_row.find_destination(50),
      52
    )
    self.assertEqual(
      map_row.find_destination(60),
      62
    )
    self.assertEqual(
      map_row.find_destination(97),
      99
    )
    self.assertEqual(
      map_row.find_destination(10),
      None
    )