import random
from abc import ABC, abstractmethod

import random_utils


class Mutation(ABC):
    @abstractmethod
    def mutate(self, individual):
        """Mutate individual in place."""


class SwitchMutation(Mutation):
    def __init__(self, frequency):
        assert frequency > 0
        self.frequency = frequency

    def mutate(self, individual):
        # mutate on average in a proportion of 1/frequency of individuals; a
        # random int in [0, frequency) is drawn, and mutation happens if it
        # equals 0 (the checked value could be anything, 0 is arbitrary)
        if random.randrange(self.frequency) == 0:
            i, j = random_utils.random_integer_pair(len(individual))
            individual[i], individual[j] = individual[j], individual[i]
