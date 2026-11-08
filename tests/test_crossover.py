import unittest
from unittest.mock import patch

from crossover import CX, OX, PMX

PARENT_A = list("ABCDEFGHIJ")
PARENT_B = list(reversed(PARENT_A))  # "JIHGFEDCBA", same genes, different order


class CrossoverStructureTestMixin:
    """Invariants every crossover operator must satisfy, regardless of which
    city ends up assigned where."""

    def test_offspring_is_permutation_of_parent_genes(self):
        offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        self.assertEqual(sorted(offspring), sorted(PARENT_A))

    def test_offspring_has_same_length_as_parents(self):
        offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        self.assertEqual(len(offspring), len(PARENT_A))

    def test_every_gene_assigned_over_many_trials(self):
        for _ in range(200):
            offspring = self.crossover.crossover(PARENT_A, PARENT_B)
            self.assertNotIn(None, offspring)
            self.assertEqual(sorted(offspring), sorted(PARENT_A))


class PMXStructureTest(CrossoverStructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.crossover = PMX()

    def test_copies_the_chosen_segment_verbatim_from_parent_a(self):
        with patch("random_utils.random_sorted_integer_pair", return_value=(2, 5)):
            offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        self.assertEqual(offspring[2:6], PARENT_A[2:6])


class OXStructureTest(CrossoverStructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.crossover = OX()

    def test_copies_the_chosen_segment_verbatim_from_parent_a(self):
        with patch("random_utils.random_sorted_integer_pair", return_value=(2, 5)):
            offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        self.assertEqual(offspring[2:6], PARENT_A[2:6])


class CXStructureTest(CrossoverStructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.crossover = CX()

    def test_every_gene_comes_from_parent_a_or_parent_b_at_its_own_position(self):
        # hallmark of cycle crossover: offspring[i] is always either
        # parentA[i] (if i is in the cycle starting at index 0) or
        # parentB[i] (otherwise)
        offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        for i, gene in enumerate(offspring):
            self.assertIn(gene, (PARENT_A[i], PARENT_B[i]))

    def test_first_gene_always_comes_from_parent_a(self):
        offspring = self.crossover.crossover(PARENT_A, PARENT_B)
        self.assertEqual(offspring[0], PARENT_A[0])


if __name__ == "__main__":
    unittest.main()
