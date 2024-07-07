from individual import Individual


class FitnessFunction:

    @staticmethod
    def evaluate_individual(individual: Individual) -> int:
        score = 0

        # Evaluate rows
        for row in individual.genotype:
            score += FitnessFunction._count_uniques(row)

        # Evaluate columns
        for col in range(len(individual.genotype)):
            column = [individual.genotype[row][col] for row in range(len(individual.genotype))]
            score += FitnessFunction._count_uniques(column)

        # Evaluate 3x3 squares
        for box_row in range(0, len(individual.genotype), 3):
            for box_col in range(0, len(individual.genotype), 3):
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(individual.genotype[box_row + i][box_col + i])
                score += FitnessFunction._count_uniques(square)

        return score

    @staticmethod
    def _count_uniques(array):
        return len(set(array))
