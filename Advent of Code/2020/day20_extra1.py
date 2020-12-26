
from day20_extra0 import *

class Tile:
    def __init__(self, img: [[str]], id: int):
        self._img = img
        self._id = id
        self._type = 'unknown'
        self._matched = False


    def get_img(self) -> [[str]]:
        '''Returns the tile image'''
        return self._img


    def get_top(self) -> str:
        '''Returns the top-most row of the tile image'''
        return self._img[0]


    def get_bottom(self) -> str:
        '''Returns the bottom-most row of the tile image'''
        return self._img[-1]


    def get_left(self) -> str:
        '''Returns the left-most column of the tile image'''
        return self._get_col(0)
    

    def get_right(self) -> str:
        '''Returns the right-most column of the tile image'''
        return self._get_col(-1)


    def get_sides(self) -> [str]:
        '''Returns a list of the tile's sides'''
        return [self.get_top(),
                self.get_bottom(),
                self.get_left(),
                self.get_right()]

    
    def _get_col(self, index: int) -> str:
        '''Returns the characters in a column as a string'''
        col = ''
        for row in self._img:
            col += row[index]
        return col
    

    def get_id(self) -> int:
        '''Returns the tile ID'''
        return self._id


    def get_type(self) -> str:
        '''Returns the tile's type (corner, edge, center)'''
        return self._type


    def set_type(self, matching_sides: int) -> None:
        '''Sets the tile's type'''
        if matching_sides == 2:
            self._type = 'corner'
        elif matching_sides == 3:
            self._type = 'edge'
        elif matching_sides == 4:
            self._type = 'center'


    def matched(self) -> bool:
        '''Returns whether the tile has been used to match'''
        return self._matched


    def set_matching(self) -> None:
        '''Sets the tile to be matched'''
        self._matched = True


    def rotate_counter_clockwise(self) -> None:
        '''Rotates the image 90 degrees'''
        rotated = []
        for i in range(len(self._img) - 1, -1, -1):
            rotated.append(self._get_col(i))
        self._img = rotated


    def rotate_clockwise(self) -> None:
        '''Rotates the image -90 degrees'''
        rotated = []
        for i in range(len(self._img)):
            rotated.append(reverse_string(self._get_col(i)))
        self._img = rotated

        
    def flip_vertical(self) -> None:
        '''Flips the image along the x-axis'''
        flipped = []
        for i in range(len(self._img) - 1, -1, -1):
            flipped.append(self._img[i])
        self._img = flipped


    def flip_horizontal(self) -> None:
        '''Flips the image along the y-axis'''
        for i in range(len(self._img)):
            self._img[i] = reverse_string(self._img[i])
        


