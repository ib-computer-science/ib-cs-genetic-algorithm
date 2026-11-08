from crossover import OX
from genetic_algorithm import TSPGeneticAlgorithm
from mutation import SwitchMutation
from selection import TruncationSelection
from termination import TerminationRuleBestMid


def main():
    population_size = 10000
    num_elites = 5

    selection = TruncationSelection(5)  # select fittest 1/5 of population
    # selection = RouletteWheelSelection(population_size // 3)
    # selection = TournamentSelection(population_size // 3, 2)

    crossover = OX()  # order crossover
    # crossover = PMX()  # partially mapped crossover
    # crossover = CX()  # cycle crossover

    # switch two random cities on the average in 1/20 individuals
    mutation = SwitchMutation(20)

    termination_rule = TerminationRuleBestMid()

    ga = TSPGeneticAlgorithm(population_size, num_elites, selection, crossover, mutation, termination_rule)
    ga.run()


if __name__ == "__main__":
    main()
