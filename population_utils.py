def sort_population(population, fitnesses):
    """Sort population and fitnesses together, fittest (highest fitness) first."""
    order = sorted(range(len(population)), key=lambda i: fitnesses[i], reverse=True)
    sorted_population = [population[i] for i in order]
    sorted_fitnesses = [fitnesses[i] for i in order]
    return sorted_population, sorted_fitnesses


def mid_value(fitnesses):
    """Quick and dirty "median"; assumes fitnesses is sorted."""
    return fitnesses[len(fitnesses) // 2]
