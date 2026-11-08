import random
from abc import ABC, abstractmethod

import random_utils
from population_utils import sort_population


class Selection(ABC):
    """Selects parents for the next generation."""

    @abstractmethod
    def select(self, population, fitnesses):
        """Select from population using fitnesses; population is sorted fittest-first."""


class TruncationSelection(Selection):
    def __init__(self, proportion):
        self.proportion = proportion

    def select(self, population, fitnesses):
        pool_size = len(population) // self.proportion
        return population[:pool_size]


class RouletteWheelSelection(Selection):
    def __init__(self, num_selected):
        self.num_selected = num_selected

    def select(self, population, fitnesses):
        # convert fitnesses into nonnegative values by subtracting the minimum
        # fitness; population is sorted, so the last individual has min fitness
        min_fitness = fitnesses[-1]
        positive_fitnesses = [f - min_fitness for f in fitnesses]
        total_fitness = sum(positive_fitnesses)

        cumulative_probs = []
        running_prob = 0.0
        for f in positive_fitnesses:
            running_prob += f / total_fitness
            cumulative_probs.append(running_prob)

        selected = []
        selected_fitnesses = []
        for _ in range(self.num_selected):
            p = random_utils.random_uniform()
            s = 0
            while cumulative_probs[s] < p:
                s += 1
            selected.append(population[s])
            selected_fitnesses.append(fitnesses[s])

        sorted_selected, _ = sort_population(selected, selected_fitnesses)
        return sorted_selected


class TournamentSelection(Selection):
    def __init__(self, num_selected, num_participants):
        self.num_selected = num_selected
        self.num_participants = num_participants

    def select(self, population, fitnesses):
        selected = []
        selected_fitnesses = []
        for _ in range(self.num_selected):
            # population is sorted fittest-first, so the smallest index wins
            winner = min(random.randrange(self.num_selected) for _ in range(self.num_participants))
            selected.append(population[winner])
            selected_fitnesses.append(fitnesses[winner])

        sorted_selected, _ = sort_population(selected, selected_fitnesses)
        return sorted_selected
