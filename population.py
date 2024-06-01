from individual import Individual


class Population:

    def __init__(self) -> None:
        pass

    def initialize(self, path_to_file, population_size=10):
        with open(path_to_file, "r") as f:
            rows = f.readlines()
            puzzle = [[int(num) for num in row.split(",")] for row in rows]
            print(puzzle)

        individual = Individual()
        print(individual)
