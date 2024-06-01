from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class Individual:
    genotype: List[List[int]]
    fixed_indices: Set[Tuple[int, int]]
