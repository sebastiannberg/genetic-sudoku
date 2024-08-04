import os
from population import Population
from tournament_selection import TournamentSelection
from mutation import Mutation


current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_puzzle = os.path.join(current_dir, "data", "puzzle_1.txt")
population = Population(path_to_puzzle, initial_population_size=10)
torunament_selection = TournamentSelection(tournament_size=3)
mutation = Mutation(mutation_probability=0.1)

selection = torunament_selection.select(population, num_selection=10)
for individual in selection:
    mutated_individual = mutation.perform(individual)
