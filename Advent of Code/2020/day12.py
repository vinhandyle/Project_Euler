# Day 12: Rain Risk
# Part 1: 998
# Part 2: 71586

from pathlib import Path

import math

INPUT = Path('input_12.txt')
DEBUG_1 = False
DEBUG_2 = False


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the Manhattan distance between the starting and ending locations.
    '''
    input_list = _get_inputs()
    x = 0
    y = 0
    deg = 0

    for input in input_list:
        type, value = input

        if DEBUG_1:
            print(f'{input}: ({x}, {y}) -> ', end = '')
            
        if type == 'N':
            y += value
        elif type == 'S':
            y -= value
        elif type == 'E':
            x += value
        elif type == 'W':
            x -= value
        elif type == 'L':
            deg += value
        elif type == 'R':
            deg -= value
        elif type == 'F':
            x += value * int(math.cos(deg * math.pi / 180))
            y += value * int(math.sin(deg * math.pi / 180))

        if DEBUG_1:
            print(f'({x}, {y})') 

    return abs(x) + abs(y)



def get_second_ans() -> int:
    '''
    Returns the Manhattan distance between the starting and ending locations when
    traveling using a waypoint.
    '''
    input_list = _get_inputs()
    x = 0
    y = 0
    way_point_x = 10
    way_point_y = 1
    deg = 0

    for input in input_list:
        type, value = input

        if DEBUG_2:
            print(f'{input}: ({x}, {y}), ({way_point_x}, {way_point_y}), {deg} -> ', end = '')
            
        if type == 'N':
            way_point_y += value
        elif type == 'S':
            way_point_y -= value
        elif type == 'E':
            way_point_x += value
        elif type == 'W':
            way_point_x -= value
        elif type == 'L':
            deg = _simplify_angle(deg + value)
            way_point_x, way_point_y = _rotate_way_point(
                way_point_x, way_point_y, value)
        elif type == 'R':
            deg = _simplify_angle(deg - value)
            way_point_x, way_point_y = _rotate_way_point(
                way_point_x, way_point_y, -value)
        elif type == 'F':
            x += value * way_point_x
            y += value * way_point_y

        if DEBUG_2:
            print(f'({x}, {y}), ({way_point_x}, {way_point_y}), {deg}') 

    return abs(x) + abs(y)



def _simplify_angle(deg: int) -> int:
    '''Returns the simplified version of an angle (0 <= deg < 360)'''
    while deg >= 360:
        deg -= 360

    while deg < 0:
        deg += 360

    return deg



def _rotate_way_point(x: int, y: int, amt: int) -> (int, int):
    '''
    Given the x and y coordinates of a waypoint and the amount to rotate it,
    returns new x and y coordinates.
    '''
    amt = _simplify_angle(amt)
    
    if amt == 0:
        return x, y
    elif amt == 90:
        return -y, x
    elif amt == 180:
        return -x, -y
    elif amt == 270:
        return y, -x



def _get_inputs() -> [(str, int)]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    tuples containing an action's type and value.
    '''
    file = open(INPUT, 'r')
    input_list = []

    for line in file:
        input_list.append((line[0], int(line[1:])))

    file.close()
    return input_list


    
if __name__ == '__main__':
    run()
