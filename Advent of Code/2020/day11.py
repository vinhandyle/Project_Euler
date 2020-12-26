# Day 11: Seating System
# Part 1: 2346
# Part 2: 2111

from pathlib import Path

INPUT = Path('input_11.txt')
DEBUG_1 = False
DEBUG_2 = False


# Seat states: . = floor, L = empty, # = occupied
class Seat:
    def __init__(self, state: str):
        self._state = state


    def get_state(self) -> str:
        return self._state


    def set_state(self, state: str) -> None:
        self._state = state



def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the number of occupied seats after enough rounds of changes'''
    waiting_area = _get_waiting_area()

    if DEBUG_1:
        _print_seats(waiting_area)
    
    while _update_seats(waiting_area):
        if DEBUG_1:
            _print_seats(waiting_area)
        else:
            pass

    return _get_occupied(waiting_area)



def get_second_ans() -> int:
    '''Returns the number of occupied seats after enough rounds of changes'''
    waiting_area = _get_waiting_area()

    if DEBUG_2:
        _print_seats(waiting_area)

    while _update_seats_better(waiting_area):
        if DEBUG_2:
            _print_seats(waiting_area)
        else:
            pass

    return _get_occupied(waiting_area)



def _print_seats(seats: [[Seat]]) -> None:
    '''Prints the state of each seat in the given 2D list'''
    for row in seats:
        for seat in row:
            print(seat.get_state(), end = '')
        print()
    print()



def _get_occupied(seats: [[Seat]]) -> int:
    '''Returns the current number of occupied seats'''
    occupied_seats = 0
    for row in seats:
        for seat in row:
            if seat.get_state() == '#':
                occupied_seats += 1
    return occupied_seats



def _update_seats_better(seats: [[Seat]]) -> bool:
    '''
    Updates the states of each seat in the given 2D list.
    Returns True if any seats were changed, return False otherwise.
    '''
    updated = False
    ref_seats = _dup_seats(seats)

    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]

            # If empty and no visible occupied -> Occupied
            if seat.get_state() == 'L' and \
               not _visible_occupied(ref_seats, row, col):
                seats[row][col].set_state('#')
                updated = True

            # If occupied and 5+ visible occupied -> Empty
            elif seat.get_state() == '#' and \
                 _visible_occupied(ref_seats, row, col) >= 5:
                seats[row][col].set_state('L')
                updated = True

    return updated



def _visible_occupied(seats: [[Seat]], row: int, col: int) -> int:
    '''
    Returns the number of occupied seats visible to the seat in the row and
    column.
    '''
    adjacent = 0
    
    if _occupied_in_direction(seats, row, col, -1, 0):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, -1, 1):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, 0, 1):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, 1, 1):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, 1, 0):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, 1, -1):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, 0, -1):
        adjacent += 1
    if _occupied_in_direction(seats, row, col, -1, -1):
        adjacent += 1

    return adjacent



def _occupied_in_direction(seats: [[Seat]], row: int, col: int, row_delta: int, col_delta: int) -> bool:
    '''
    Returns True if the first visible seat in a given direction relative to
    the given row and column is occupied.
    Returns False otherwise.
    '''
    occupied = False
    i = 1

    while True:
        _row = row + row_delta * i
        _col = col + col_delta * i

        # If the index is valid, checks if it is a seat
        # Occupied = True, Empty = False, Floor = Continue
        if 0 <= _row < len(seats) and 0 <= _col < len(seats[0]):
            seat = seats[_row][_col]
            if seat.get_state() == '#':
                occupied = True
                break
            elif seat.get_state() == 'L':
                break
            else:
                i += 1
        else:
            break

    return occupied



def _update_seats(seats: [[Seat]]) -> bool:
    '''
    Updates the states of each seat in the given 2D list.
    Returns True if any seats were changed, return False otherwise.
    '''
    updated = False
    ref_seats = _dup_seats(seats)

    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]

            # If empty and no adjacent occupied -> Occupied
            if seat.get_state() == 'L' and \
               not _adjacent_occupied(ref_seats, row, col):
                seats[row][col].set_state('#')
                updated = True

            # If occupied and 4+ adjacent occupied -> Empty
            elif seat.get_state() == '#' and \
                 _adjacent_occupied(ref_seats, row, col) >= 4:
                seats[row][col].set_state('L')
                updated = True

    return updated
    


def _adjacent_occupied(seats: [[Seat]], row: int, col: int) -> int:
    '''
    Returns the number of occupied seats adjacent to the seat in the row and
    column.
    '''
    adjacent = 0
    adjacent_indexes = [(row - 1, col),
                        (row - 1, col + 1),
                        (row, col + 1),
                        (row + 1, col + 1),
                        (row + 1, col),
                        (row + 1, col - 1),
                        (row, col - 1),
                        (row - 1, col - 1)]

    valid_indexes = []

    # Remove erroneous indexes
    for index in adjacent_indexes:
        _row, _col = index
        if 0 <= _row < len(seats) and 0 <= _col < len(seats[0]):
            valid_indexes.append(index)

    # Check seat states
    for index in valid_indexes:
        _row, _col = index
        seat = seats[_row][_col]

        if seat.get_state() == '#':
            adjacent += 1
    return adjacent



def _dup_seats(seats: [[Seat]]) -> [[Seat]]:
    '''Returns a copy of the given seats'''
    new_seats = []
    for row in seats:
        new_row = []
        for seat in row:
            new_row.append(Seat(seat.get_state()))
        new_seats.append(new_row)
    return new_seats



def _get_waiting_area() -> [[Seat]]:
    '''
    Finds the text file specified by INPUT and returns its content as a 2D list
    of Seat objects.
    '''
    file = open(INPUT, 'r')
    waiting_area = []

    for line in file:
        row = []
        for char in line:
            row.append(Seat(char))
        waiting_area.append(row)  

    file.close()
    return waiting_area



if __name__ == '__main__':
    run()
