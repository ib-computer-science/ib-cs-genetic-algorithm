import unittest

from population_utils import mid_value, sort_population


class SortPopulationTest(unittest.TestCase):
    def test_sorts_fittest_first(self):
        population = ["c", "a", "b"]
        fitnesses = [-30, -10, -20]
        sorted_population, sorted_fitnesses = sort_population(population, fitnesses)
        self.assertEqual(sorted_population, ["a", "b", "c"])
        self.assertEqual(sorted_fitnesses, [-10, -20, -30])

    def test_population_and_fitnesses_stay_paired(self):
        population = ["route1", "route2", "route3", "route4"]
        fitnesses = [-5, -1, -9, -3]
        sorted_population, sorted_fitnesses = sort_population(population, fitnesses)
        pairing = dict(zip(population, fitnesses))
        for route, fitness in zip(sorted_population, sorted_fitnesses):
            self.assertEqual(pairing[route], fitness)

    def test_preserves_length(self):
        population = list(range(7))
        fitnesses = list(range(7))
        sorted_population, sorted_fitnesses = sort_population(population, fitnesses)
        self.assertEqual(len(sorted_population), 7)
        self.assertEqual(len(sorted_fitnesses), 7)


class MidValueTest(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(mid_value([5, 4, 3, 2, 1]), 3)

    def test_even_length(self):
        self.assertEqual(mid_value([4, 3, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()
