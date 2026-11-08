import unittest
from unittest.mock import patch

from selection import RouletteWheelSelection, TournamentSelection, TruncationSelection

# already sorted fittest (least negative) first, as the real population would be
POPULATION = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
FITNESSES = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]


class TruncationSelectionTest(unittest.TestCase):
    def test_selects_the_fittest_fraction(self):
        selected = TruncationSelection(5).select(POPULATION, FITNESSES)
        self.assertEqual(selected, POPULATION[:2])  # 10 // 5 == 2

    def test_proportion_one_selects_everyone(self):
        selected = TruncationSelection(1).select(POPULATION, FITNESSES)
        self.assertEqual(selected, POPULATION)


class RouletteWheelSelectionTest(unittest.TestCase):
    def test_returns_the_requested_number_of_individuals(self):
        selected = RouletteWheelSelection(4).select(POPULATION, FITNESSES)
        self.assertEqual(len(selected), 4)
        for individual in selected:
            self.assertIn(individual, POPULATION)

    def test_result_is_sorted_fittest_first(self):
        with patch("random_utils.random_uniform", side_effect=[0.95, 0.05, 0.5]):
            selected = RouletteWheelSelection(3).select(POPULATION, FITNESSES)
        selected_fitnesses = [FITNESSES[POPULATION.index(ind)] for ind in selected]
        self.assertEqual(selected_fitnesses, sorted(selected_fitnesses, reverse=True))

    def test_probability_zero_always_selects_the_fittest_individual(self):
        with patch("random_utils.random_uniform", return_value=0.0):
            selected = RouletteWheelSelection(1).select(POPULATION, FITNESSES)
        self.assertEqual(selected, [POPULATION[0]])


class TournamentSelectionTest(unittest.TestCase):
    def test_returns_the_requested_number_of_individuals(self):
        selected = TournamentSelection(5, 3).select(POPULATION, FITNESSES)
        self.assertEqual(len(selected), 5)

    def test_only_draws_participants_from_the_first_num_selected_individuals(self):
        selection = TournamentSelection(4, 3)
        allowed = set(POPULATION[:4])
        for _ in range(100):
            selected = selection.select(POPULATION, FITNESSES)
            self.assertTrue(set(selected) <= allowed)

    def test_lower_sampled_index_always_wins_the_tournament(self):
        # population is sorted fittest-first, so the smallest sampled index
        # must win; two tournaments of two participants each
        with patch("random.randrange", side_effect=[1, 0, 0, 1]):
            selected = TournamentSelection(2, 2).select(POPULATION, FITNESSES)
        # tournament 1: samples (1, 0) -> winner index 0
        # tournament 2: samples (0, 1) -> winner index 0
        self.assertEqual(selected, [POPULATION[0], POPULATION[0]])


if __name__ == "__main__":
    unittest.main()
