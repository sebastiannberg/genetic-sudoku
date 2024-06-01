from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Individual:
    genotype: List[List[int]]
    fixed_indices: Set[Tuple[int, int]]
    non_fixed_indices: Set[Tuple[int, int]]

    def display_phenotype(self):
        for i, row in enumerate(self.genotype):
            if i in [3, 6]:
                print('------+-------+------')
            for j, value in enumerate(row):
                if j in [3, 6]:
                    print('|', end=' ')
                print(value, end=' ')
            print()
        print()
