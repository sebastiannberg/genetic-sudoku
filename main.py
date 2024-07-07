import os
from population import Population
from fitness_function import FitnessFunction


current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_puzzle = os.path.join(current_dir, "data", "puzzle_1.txt")
population = Population(path_to_puzzle, initial_population_size=10)

population_fitness = sum(FitnessFunction.evaluate_individual(individual) for individual in population.individuals)
print(population_fitness)
for individual in population.individuals:
    fitness = FitnessFunction.evaluate_individual(individual)
    print(fitness)
