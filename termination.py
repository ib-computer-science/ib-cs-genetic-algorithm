from abc import ABC, abstractmethod

from population_utils import mid_value


class TerminationRule(ABC):
    @abstractmethod
    def terminates(self, parent_fitnesses, offspring_fitnesses):
        """Return True if the algorithm should stop."""


class TerminationRuleBestMid(TerminationRule):
    """Terminates if there is no improvement in the fittest individual and
    no improvement in "median" fitness from the previous generation; assumes
    fitness lists are sorted in decreasing order."""

    def terminates(self, parent_fitnesses, offspring_fitnesses):
        return (offspring_fitnesses[0] <= parent_fitnesses[0]
                and mid_value(offspring_fitnesses) <= mid_value(parent_fitnesses))
