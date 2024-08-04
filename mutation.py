import random
from copy import deepcopy

from individual import Individual


class Mutation:

    def __init__(self, mutation_probability: float) -> None:
        self.mutation_probability = mutation_probability

    def perform(self, individual: Individual):
        mutated_individual = deepcopy(individual)

        for indices in mutated_individual.non_fixed_indices:
            if (random.random() <= self.mutation_probability):
                mutated_individual.genotype[indices[0]][indices[1]] = random.randint(1,9)
        return mutated_individual
