import random
import unittest
from unittest.mock import patch

import two_opt
from distances import DISTANCES, STARTCITY, VISITED_CITIES

# hand-verified against the real distance table:
# ["A", "C", "B", "D"] has length 663 and its only improving move is
# reversing [0:3) (delta -121), landing on ["B", "C", "A", "D"] (length 542);
# from there the only improving move is reversing [0:2) (delta -10), landing
# on ["C", "B", "A", "D"] (length 532), which is itself 2-opt-optimal.
CROSSED_ROUTE = ["A", "C", "B", "D"]
OPTIMAL_ROUTE = ["C", "B", "A", "D"]


class RouteLengthTest(unittest.TestCase):
    def test_matches_hand_computed_distance(self):
        route = list(VISITED_CITIES)
        expected = DISTANCES[STARTCITY][route[0]] + DISTANCES[STARTCITY][route[-1]]
        for city_a, city_b in zip(route, route[1:]):
            expected += DISTANCES[city_a][city_b]
        self.assertEqual(two_opt.route_length(route), expected)

    def test_length_is_always_positive(self):
        self.assertGreater(two_opt.route_length(list(VISITED_CITIES)), 0)

    def test_matches_hand_verified_example(self):
        self.assertEqual(two_opt.route_length(CROSSED_ROUTE), 663)
        self.assertEqual(two_opt.route_length(OPTIMAL_ROUTE), 532)


class BestMoveTest(unittest.TestCase):
    def test_identifies_the_best_improving_move(self):
        self.assertEqual(two_opt._best_move(CROSSED_ROUTE), (-121, 0, 2))

    def test_returns_none_when_route_is_already_locally_optimal(self):
        self.assertEqual(two_opt._best_move(OPTIMAL_ROUTE), (0, None, None))


class LocalSearchTest(unittest.TestCase):
    def test_corrects_a_crossed_route_into_the_locally_optimal_one(self):
        route = CROSSED_ROUTE[:]
        two_opt.local_search(route)
        self.assertEqual(route, OPTIMAL_ROUTE)
        self.assertEqual(two_opt.route_length(route), 532)

    def test_leaves_an_already_optimal_route_unchanged(self):
        route = OPTIMAL_ROUTE[:]
        two_opt.local_search(route)
        self.assertEqual(route, OPTIMAL_ROUTE)

    def test_always_leaves_a_permutation_of_the_same_genes(self):
        for _ in range(50):
            route = list(VISITED_CITIES)
            random_order = route[:]
            random.shuffle(random_order)
            two_opt.local_search(random_order)
            self.assertEqual(sorted(random_order), sorted(route))


class SolveTest(unittest.TestCase):
    def test_num_restarts_must_be_positive(self):
        with self.assertRaises(AssertionError):
            two_opt.solve(0)

    def test_returns_a_valid_permutation_of_visited_cities(self):
        route, length = two_opt.solve(5)
        self.assertEqual(sorted(route), sorted(VISITED_CITIES))
        self.assertEqual(length, two_opt.route_length(route))

    def test_picks_the_shortest_result_across_restarts(self):
        cities = list(VISITED_CITIES)
        candidate_a = cities[:]
        candidate_b = list(reversed(cities))
        candidate_c = cities[:3] + list(reversed(cities[3:]))
        candidates = [candidate_a, candidate_b, candidate_c]

        shuffles = iter(candidates)

        def fake_shuffle(seq):
            seq[:] = next(shuffles)

        lengths = [two_opt.route_length(c) for c in candidates]
        expected_route = candidates[lengths.index(min(lengths))]

        with patch("random.shuffle", side_effect=fake_shuffle), \
                patch("two_opt.local_search"):  # no-op: keep routes as shuffled
            route, length = two_opt.solve(3)

        self.assertEqual(route, expected_route)
        self.assertEqual(length, min(lengths))


class RouteToStringTest(unittest.TestCase):
    def test_wraps_route_with_startcity(self):
        route = list(VISITED_CITIES)
        self.assertEqual(two_opt._route_to_string(route), STARTCITY + VISITED_CITIES + STARTCITY)


if __name__ == "__main__":
    unittest.main()
