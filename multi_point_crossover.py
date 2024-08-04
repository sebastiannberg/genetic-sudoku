import random
from typing import Tuple
from copy import deepcopy

from individual import Individual


class MultiPointCrossover:

    def __init__(self, num_crossover_points: int) -> None:
        self.num_crossover_points = num_crossover_points

    def perform(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        offspring1 = deepcopy(parent1)
        offspring2 = deepcopy(parent2)

        non_fixed_indices = offspring1.non_fixed_indices
        crossover_points = random.sample(non_fixed_indices, k=self.num_crossover_points)

        for indices in crossover_points:
            offspring1.genotype[indices[0]][indices[1]], offspring2.genotype[indices[0]][indices[1]] = (
            offspring2.genotype[indices[0]][indices[1]],
            offspring1.genotype[indices[0]][indices[1]]
        )

        return offspring1, offspring2
