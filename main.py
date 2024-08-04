import os

from population import Population
from tournament_selection import TournamentSelection
from mutation import Mutation
from fitness_function import FitnessFunction
from multi_point_crossover import MultiPointCrossover

current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_puzzle = os.path.join(current_dir, "data", "puzzle_1.txt")
population = Population(path_to_puzzle, initial_population_size=300)
tournament_selection = TournamentSelection(tournament_size=20)
mutation = Mutation(mutation_probability=0.01)
crossover = MultiPointCrossover(num_crossover_points=30)

while True:
    selection = tournament_selection.select(population, num_selection=300)
    next_generation = []
    for i in range(0, len(selection), 2):
        parent1 = selection[i]
        parent2 = selection[i + 1] if i + 1 < len(selection) else selection[0]
        offspring1, offspring2 = crossover.perform(parent1, parent2)
        mutated_individual1 = mutation.perform(offspring1)
        mutated_individual2 = mutation.perform(offspring2)
        next_generation.extend([mutated_individual1, mutated_individual2])

    population.update(next_generation)
    population_score = FitnessFunction.evaluate_population(population)
    print(population_score)
    if population_score >= 200:
        best_individual = max(population.individuals, key=FitnessFunction.evaluate_individual)
        best_individual.display_phenotype()
        break
