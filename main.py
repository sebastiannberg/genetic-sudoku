import os
from population import Population


current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_puzzle = os.path.join(current_dir, "data", "puzzle_1.txt")
population = Population(path_to_puzzle)
