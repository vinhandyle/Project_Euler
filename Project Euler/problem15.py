# Problem 15: Lattice paths
# Answer: 137846528820

import math

GRID = 20


def run() -> None:
    # Combination
    print(math.factorial(GRID * 2) /
          (math.factorial(GRID) * math.factorial(GRID)))



if __name__ == '__main__':
    run()


