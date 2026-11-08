from abc import ABC, abstractmethod

import random_utils


class Crossover(ABC):
    @abstractmethod
    def crossover(self, parent_a, parent_b):
        """Return a new offspring route combining genes from both parents."""


class PMX(Crossover):
    """Partially mapped crossover."""

    def crossover(self, parent_a, parent_b):
        a_start, a_end = random_utils.random_sorted_integer_pair(len(parent_a))
        a_segment = parent_a[a_start:a_end + 1]

        offspring = [None] * len(parent_a)
        b_ind = 0
        for i in range(len(offspring)):
            if a_start <= i <= a_end:
                offspring[i] = parent_a[i]
            else:
                while parent_b[b_ind] in a_segment:
                    b_ind += 1
                offspring[i] = parent_b[b_ind]
                b_ind += 1

        return offspring


class OX(Crossover):
    """Order crossover."""

    def crossover(self, parent_a, parent_b):
        n = len(parent_a)
        a_start, a_end = random_utils.random_sorted_integer_pair(n)
        a_segment = set(parent_a[a_start:a_end + 1])

        offspring = [None] * n
        for i in range(a_start, a_end + 1):
            offspring[i] = parent_a[i]

        offspring_ind = (a_end + 1) % n
        b_ind = (a_end + 1) % n
        num_assigned = a_end - a_start + 1

        while num_assigned < n:
            while parent_b[b_ind] in a_segment:
                b_ind = (b_ind + 1) % n
            offspring[offspring_ind] = parent_b[b_ind]
            num_assigned += 1
            b_ind = (b_ind + 1) % n
            offspring_ind = (offspring_ind + 1) % n

        return offspring


class CX(Crossover):
    """Cycle crossover."""

    def crossover(self, parent_a, parent_b):
        offspring = [None] * len(parent_a)
        assigned = [False] * len(parent_a)
        offspring[0] = parent_a[0]
        assigned[0] = True

        c = parent_b[0]
        i = parent_a.index(c)
        while i != 0:
            offspring[i] = c
            assigned[i] = True
            c = parent_b[i]
            i = parent_a.index(c)

        # copy remaining genes from parent B
        for j in range(len(offspring)):
            if not assigned[j]:
                offspring[j] = parent_b[j]

        return offspring
