import random

import random_utils
from distances import DISTANCES, STARTCITY, VISITED_CITIES
from population_utils import mid_value, sort_population


class TSPGeneticAlgorithm:
    def __init__(self, population_size, num_elites, selection, crossover, mutation, termination_rule):
        """mutation may be None if no mutation is desired."""
        self.population_size = population_size
        self.num_elites = num_elites
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.termination_rule = termination_rule

    def run(self):
        population, fitnesses = self._evaluate(self._initialize_population())

        generation = 0
        terminate = False
        while not terminate:
            generation += 1

            # diagnostic stats printed for every generation
            print(f"gen [ {generation} ] fit [ {fitnesses[0]} ] "
                  f"best [ {self._route_to_string(population[0])} ] "
                  f"mid [ {mid_value(fitnesses)} ]")

            # selection and crossover
            parents = self.selection.select(population, fitnesses)
            offspring = self._reproduce(parents, population)

            # mutation if so desired
            if self.mutation is not None:
                for i in range(self.num_elites, self.population_size):  # elites not mutated
                    self.mutation.mutate(offspring[i])

            # evaluation of new generation
            offspring_population, offspring_fitnesses = self._evaluate(offspring)

            # check for termination
            terminate = self.termination_rule.terminates(fitnesses, offspring_fitnesses)

            # current offspring forms population
            population, fitnesses = offspring_population, offspring_fitnesses

        return population, fitnesses

    def _initialize_population(self):
        """Return population with random permutations of visited cities."""
        cities = list(VISITED_CITIES)
        population = []
        for _ in range(self.population_size):
            random.shuffle(cities)
            population.append(list(cities))
        return population

    def _evaluate(self, population):
        """Evaluate, sort and return sorted population and sorted fitnesses;
        fitness is the opposite of route length (negative), so maximizing
        fitness minimizes route length."""
        fitnesses = [self._route_fitness(route) for route in population]
        return sort_population(population, fitnesses)

    @staticmethod
    def _route_fitness(route):
        fitness = -DISTANCES[STARTCITY][route[0]] - DISTANCES[STARTCITY][route[-1]]
        for city_a, city_b in zip(route, route[1:]):
            fitness -= DISTANCES[city_a][city_b]
        return fitness

    def _reproduce(self, parents, population):
        # elites carry over unchanged into the next generation
        offspring = list(population[:self.num_elites])

        num_parents = len(parents)
        while len(offspring) < self.population_size:
            i, j = random_utils.random_integer_pair(num_parents)
            offspring.append(self.crossover.crossover(parents[i], parents[j]))

        return offspring

    @staticmethod
    def _route_to_string(route):
        return STARTCITY + "".join(route) + STARTCITY
