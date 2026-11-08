import unittest
from unittest.mock import patch

from mutation import SwitchMutation


class SwitchMutationTest(unittest.TestCase):
    def test_frequency_must_be_positive(self):
        with self.assertRaises(AssertionError):
            SwitchMutation(0)

    def test_always_leaves_a_permutation_of_the_same_genes(self):
        mutation = SwitchMutation(3)
        for _ in range(300):
            individual = list("ABCDEFGHIJ")
            original = individual[:]
            mutation.mutate(individual)
            self.assertEqual(sorted(individual), sorted(original))

    def test_swaps_exactly_the_sampled_positions_when_triggered(self):
        mutation = SwitchMutation(1)  # frequency 1 -> randrange(1) is always 0, always triggers
        individual = list("ABCDEFGHIJ")
        expected = individual[:]
        expected[2], expected[7] = expected[7], expected[2]

        with patch("random_utils.random_integer_pair", return_value=(2, 7)):
            mutation.mutate(individual)

        self.assertEqual(individual, expected)

    def test_leaves_individual_unchanged_when_not_triggered(self):
        mutation = SwitchMutation(1000)
        individual = list("ABCDEFGHIJ")
        original = individual[:]

        with patch("random.randrange", return_value=1):  # force the "no mutation" branch
            mutation.mutate(individual)

        self.assertEqual(individual, original)


if __name__ == "__main__":
    unittest.main()
