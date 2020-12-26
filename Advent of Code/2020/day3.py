# Day 3: Toboggan Trajectory
# Part 1: 171
# Part 2: 1206576000

from pathlib import Path


INPUT = Path('input_3.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())


def get_first_ans() -> int:
    '''
    Returns the number of trees encountered, starting at the top-left corner of
    the map and following a slope of right 3 and down 1.
    '''
    tree_map = _get_tree_map()
    return _trees_in_the_way(tree_map, 3, 1)


def get_second_ans() -> int:
    '''
    Returns the number of trees encountered, starting at the top-left corner of
    the map and following multiple slopes.
    '''
    tree_map = _get_tree_map()
    return _trees_in_the_way(tree_map, 1, 1) * \
           _trees_in_the_way(tree_map, 3, 1) * \
           _trees_in_the_way(tree_map, 5, 1) * \
           _trees_in_the_way(tree_map, 7, 1) * \
           _trees_in_the_way(tree_map, 1, 2)



def _trees_in_the_way(tree_map: [[str]], right: int, down: int) -> int:
    '''
    Returns the number of trees encountered, starting at the top-left corner of
    the map and following a slope of right x and down y.
    '''
    trees = 0
    row = 0
    col = 0

    while row < len(tree_map):
        # Wrap around back to left end of map
        if col >= len(tree_map[row]):
            col -= len(tree_map[row])
            
        area = tree_map[row][col]
        if area == '#':
            trees += 1

        row += down
        col += right

    return trees



def _get_tree_map() -> [[str]]:
    '''
    Finds the text file specified by INPUT and returns its content as a nested
    list of strings.
    '''
    tree_map = []
    file = open(INPUT, 'r')

    for line in file:
        map_section = []
        for char in line[:-1]:
            map_section.append(char)
        tree_map.append(map_section)

    file.close()
    return tree_map


    
if __name__ == '__main__':
    run()


