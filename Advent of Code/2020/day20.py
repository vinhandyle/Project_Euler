# Day 20: Jurassic Jigsaw
# Part 1: 54755174472007
# Part 2: 1692 (1707)

from pathlib import Path
from day20_extra1 import Tile
from day20_extra2 import Jigsaw
from day20_extra3 import Map

INPUT = Path('input_20.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())
    


def get_first_ans() -> int:
    '''
    Returns the product of the IDs of the corner tiles after assembling the full
    image successfully.
    '''
    jigsaw = Jigsaw(_get_tiles())
    jigsaw.arrange_by_type()
    jigsaw.complete()
    
    return jigsaw.product_of_corners()
    

def get_second_ans() -> int:
    '''
    Returns the number of #s in the image that are not part of a sea monster.
    '''
    jigsaw = Jigsaw(_get_tiles())
    jigsaw.arrange_by_type()
    jigsaw.complete()

    map = Map(jigsaw)
    map.mark_monsters()
    #map.display_image()
    return map.count_roughness()

    

def _get_tiles() -> [Tile]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    Tiles.
    '''
    file = open(INPUT, 'r')
    tile_list = []
    
    tile_id = 0
    tile_img = []
    for line in file:
        if len(line) == 1:
            tile_list.append(Tile(tile_img, tile_id))
            tile_img = []
            
        elif line[0:4] == 'Tile':
            tile_id = int(line[5:-2])

        else:
            if line[-1] == '\n':
                tile_img.append(line[:-1])
            else:
                tile_img.append(line)

    if tile_img != []:
        tile_list.append(Tile(tile_img, tile_id))
    
    file.close()
    return tile_list



if __name__ == '__main__':
    run()
