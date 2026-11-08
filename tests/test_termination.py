import unittest

from termination import TerminationRuleBestMid


class TerminationRuleBestMidTest(unittest.TestCase):
    def setUp(self):
        self.rule = TerminationRuleBestMid()

    def test_does_not_terminate_when_best_improves(self):
        parent = [-100, -150, -200, -250, -300]
        offspring = [-90, -150, -200, -250, -300]  # better best, same mid
        self.assertFalse(self.rule.terminates(parent, offspring))

    def test_does_not_terminate_when_mid_improves(self):
        parent = [-100, -150, -200, -250, -300]
        offspring = [-100, -150, -190, -250, -300]  # same best, better mid
        self.assertFalse(self.rule.terminates(parent, offspring))

    def test_terminates_when_neither_improves(self):
        parent = [-100, -150, -200, -250, -300]
        offspring = [-100, -160, -210, -250, -300]  # best unchanged, mid worse
        self.assertTrue(self.rule.terminates(parent, offspring))

    def test_terminates_when_generations_are_identical(self):
        fitnesses = [-100, -150, -200, -250, -300]
        self.assertTrue(self.rule.terminates(fitnesses, list(fitnesses)))


if __name__ == "__main__":
    unittest.main()
