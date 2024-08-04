from typing import List
import random

from individual import Individual


class Population:

    def __init__(self, path_to_puzzle, initial_population_size=10):
        with open(path_to_puzzle, "r") as f:
            rows = f.readlines()
            puzzle = [[int(num) for num in row.split(",")] for row in rows]

        fixed_indices = set()
        non_fixed_indices = set()
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if puzzle[i][j] != 0:
                    fixed_indices.add((i, j))
                else:
                    non_fixed_indices.add((i, j))

        individuals = []
        for _ in range(initial_population_size):
            genotype = [row[:] for row in puzzle]  # Deep copy of the puzzle
            for index_pair in non_fixed_indices:
                num = random.randint(1, 9)
                genotype[index_pair[0]][index_pair[1]] = num

            individual = Individual(genotype=genotype, fixed_indices=fixed_indices, non_fixed_indices=non_fixed_indices)
            individuals.append(individual)

        self.individuals: List[Individual] = individuals

    def update(self, individuals: List[Individual]):
        self.individuals = individuals
