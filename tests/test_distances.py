import unittest

from distances import CITIES, DISTANCES, STARTCITY, VISITED_CITIES


class DistancesStructureTest(unittest.TestCase):
    def test_city_list_is_consistent(self):
        self.assertEqual(CITIES[0], STARTCITY)
        self.assertEqual(CITIES, STARTCITY + VISITED_CITIES)
        self.assertEqual(len(CITIES), len(set(CITIES)))  # no duplicate cities

    def test_every_city_has_a_full_row(self):
        for city in CITIES:
            self.assertIn(city, DISTANCES)
            self.assertEqual(set(DISTANCES[city].keys()), set(CITIES))

    def test_distance_to_self_is_zero(self):
        for city in CITIES:
            self.assertEqual(DISTANCES[city][city], 0)

    def test_distances_are_symmetric(self):
        for city_a in CITIES:
            for city_b in CITIES:
                self.assertEqual(DISTANCES[city_a][city_b], DISTANCES[city_b][city_a])

    def test_distances_are_nonnegative(self):
        for city_a in CITIES:
            for city_b in CITIES:
                self.assertGreaterEqual(DISTANCES[city_a][city_b], 0)


if __name__ == "__main__":
    unittest.main()
