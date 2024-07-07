from typing import List
import random

from individual import Individual
from population import Population
from fitness_function import FitnessFunction


class TournamentSelection:

    def __init__(self, tournament_size: int) -> None:
        self.tournament_size = tournament_size

    def select(self, population: Population, num_offspring: int) -> List[Individual]:
        selection = []

        for _ in range(num_offspring):
            tournament = random.sample(population.individuals, k=self.tournament_size)
            fitness_scores = [(individual, FitnessFunction.evaluate_individual(Individual)) for individual in tournament]
            best_individual = max(fitness_scores, key=lambda x: x[1])[0]
            selection.append(best_individual)

        return selection
