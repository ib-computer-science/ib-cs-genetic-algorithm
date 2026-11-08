import contextlib
import io
import unittest

from crossover import OX
from distances import DISTANCES, STARTCITY, VISITED_CITIES
from genetic_algorithm import TSPGeneticAlgorithm
from mutation import SwitchMutation
from selection import TruncationSelection
from termination import TerminationRuleBestMid


def make_algorithm(population_size=40, num_elites=2):
    return TSPGeneticAlgorithm(
        population_size,
        num_elites,
        TruncationSelection(5),
        OX(),
        SwitchMutation(20),
        TerminationRuleBestMid(),
    )


class InitializePopulationTest(unittest.TestCase):
    def test_every_individual_is_a_permutation_of_visited_cities(self):
        ga = make_algorithm()
        population = ga._initialize_population()
        self.assertEqual(len(population), ga.population_size)
        for route in population:
            self.assertEqual(sorted(route), sorted(VISITED_CITIES))


class RouteFitnessTest(unittest.TestCase):
    def test_matches_hand_computed_distance(self):
        ga = make_algorithm()
        route = list(VISITED_CITIES)
        expected = -DISTANCES[STARTCITY][route[0]] - DISTANCES[STARTCITY][route[-1]]
        for city_a, city_b in zip(route, route[1:]):
            expected -= DISTANCES[city_a][city_b]
        self.assertEqual(ga._route_fitness(route), expected)

    def test_fitness_is_never_positive(self):
        ga = make_algorithm()
        route = list(VISITED_CITIES)
        self.assertLessEqual(ga._route_fitness(route), 0)


class EvaluateTest(unittest.TestCase):
    def test_sorts_population_by_recomputed_fitness(self):
        ga = make_algorithm()
        population = ga._initialize_population()
        sorted_population, sorted_fitnesses = ga._evaluate(population)
        self.assertEqual(
            sorted_fitnesses,
            [ga._route_fitness(route) for route in sorted_population],
        )
        self.assertEqual(sorted_fitnesses, sorted(sorted_fitnesses, reverse=True))


class ReproduceTest(unittest.TestCase):
    def test_elites_carry_over_unchanged(self):
        ga = make_algorithm(population_size=20, num_elites=3)
        population, fitnesses = ga._evaluate(ga._initialize_population())
        parents = ga.selection.select(population, fitnesses)
        offspring = ga._reproduce(parents, population)
        self.assertEqual(offspring[:3], population[:3])
        self.assertEqual(len(offspring), ga.population_size)


class RunTest(unittest.TestCase):
    def test_terminates_and_returns_a_valid_population(self):
        ga = make_algorithm(population_size=30, num_elites=2)
        with contextlib.redirect_stdout(io.StringIO()):
            population, fitnesses = ga.run()
        self.assertEqual(len(population), 30)
        self.assertEqual(len(fitnesses), 30)
        for route in population:
            self.assertEqual(sorted(route), sorted(VISITED_CITIES))
        self.assertEqual(fitnesses, sorted(fitnesses, reverse=True))


if __name__ == "__main__":
    unittest.main()
