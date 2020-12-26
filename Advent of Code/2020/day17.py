# Day 17: Conway Cubes
# Part 1: 426
# Part 2: 1892

from pathlib import Path

from day17_extra1 import ConwayCube
from day17_extra2 import Universe
from day17_extra3 import Hyperverse

INPUT = Path('input_17.txt')
DEBUG1 = False
DEBUG2 = False    

         
def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the number of active cubes in a 3D space after the sixth cycle'''
    total_cycles = 6
    center = _get_init()
    universe = Universe(center)
    universe.expand(total_cycles)
    
    if DEBUG1:
        print('Before any cycles:')
        universe.display_layers()

    cycles = 1
    while cycles <= total_cycles:
        universe.update()
        
        if DEBUG1:
            print(f'After {cycles} cycles:')
            universe.display_layers()
            
        cycles += 1

    return universe.count_active()
            


def get_second_ans() -> int:
    '''Returns the number of active cubes in a 4D space after the sixth cycle'''
    total_cycles = 6
    center = _get_init()
    hyperverse = Hyperverse(center)
    hyperverse.expand(total_cycles)

    if DEBUG2:
        print('Before any cycles:')
        hyperverse.display_layers()

    cycles = 1
    while cycles <= total_cycles:
        hyperverse.update()

        if DEBUG2:
            print(f'After {cycles} cycles:')
            hyperverse.display_layers()

        cycles += 1

    return hyperverse.count_active()



def _get_init() -> [[ConwayCube]]:
    '''
    Finds the text file specified by INPUT and returns its content as a matrix
    of Conway Cubes.
    '''
    file = open(INPUT, 'r')
    center = []

    for line in file:
        row = []
        for char in line:
            if char == '.':
                row.append(ConwayCube())
            elif char == '#':
                row.append(ConwayCube(True))
        center.append(row)

    file.close()
    return center



if __name__ == '__main__':
    run()
