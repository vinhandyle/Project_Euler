# Day 24: Lobby Layout
# Part 1: 312
# Part 2: 3733

from pathlib import Path

INPUT = Path('input_24.txt')
action_map = {'e': (1,0), 'se': (0.5,-1), 'sw': (-0.5,-1), \
              'w': (-1,0), 'nw': (-0.5,1), 'ne': (0.5,1)}



def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    arr = get_input()
    tiles = process(arr)
    return len(tiles)



def get_second_ans() -> int:
    arr = get_input()
    tiles = process(arr)

    for i in range(100):
        tiles = update_day(tiles)
    return len(tiles)



def find_tile(actions):
    pos = (0,0)
    for action in actions:
        delta = action_map[action]
        pos = (pos[0] + delta[0], pos[1] + delta[1])
    return pos

assert find_tile(['e', 'se', 'w']) == (0.5,-1)
assert find_tile(['nw', 'w', 'sw', 'e', 'e']) == (0,0)



def process(arr):  
    tiles = set()
    for actions in arr:
        tile = find_tile(actions)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)
    return tiles



def update_day(tiles):
    overlap = dict()
    for tile in tiles:
        for delta in action_map.values():
            n = (tile[0] + delta[0], tile[1] + delta[1])
            if n not in overlap:
                overlap[n] = 0
            overlap[n] += 1

    new_tiles = set()
    for tile, o in overlap.items():
        if tile in tiles:
            if not (o == 0 or o > 2):
                new_tiles.add(tile)
        elif o == 2:
            new_tiles.add(tile)
    return new_tiles
    


def get_input():
    file = open(INPUT, 'r')
    arr = []
    
    for line in file:
        actions, i = [], 0
        while i < len(line.rstrip()):
            if line[i] in ('n', 's'):
                actions.append(line[i:i+2])
                i += 1
            else:
                actions.append(line[i])
            i += 1
        arr.append(actions)

    file.close()
    return arr



if __name__ == '__main__':
    run()
