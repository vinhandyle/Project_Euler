
from day20_extra0 import *
from day20_extra1 import Tile
from day20_extra2 import Jigsaw

class Map:
    def __init__(self, board: [[Tile]]):
        self._image = self._create_image(board)


    def get_image(self) -> [[str]]:
        '''Returns a 2D list of characters, representing the image'''
        return self._image

    
    def _create_image(self, board: [[Tile]]) -> [[str]]:
        '''
        Creates the full image by combining each tile and removing the border.
        '''
        full_image = self._strip_and_combine_tiles(board)
        return self._listify_image(full_image)


    def display_image(self) -> None:
        '''Displays the image'''
        for row in self._image:
            for char in row:
                print(char, end = '')
            print()


    def count_roughness(self) -> int:
        '''Returns the number of #'s are in the image'''
        count = {'.': 0, '#': 0, 'O': 0}
        for row in self._image:
            for char in row:
                count[char] += 1
        return count

    
    def mark_monsters(self) -> None:
        '''
        Checks for monsters and replaces their #'s with O's.
        If no monsters appear, change the orientation of the image and try
        again.
        '''        
        monsters = self._check_for_monsters()

        if monsters == 0:
            self.flip_vertical()

        monsters = self._check_for_monsters()

        if monsters == 0:
            self.flip_horizontal()

        monsters = self._check_for_monsters()


    def _check_for_monsters(self) -> int:
        monsters = 0
        for i in range(4):
            for row in range(len(self._image)):
                for col in range(len(self._image)):
                    char = self._image[row][col]
                    if char == '#' or char == 'O':
                        if self._check_for_monster(row, col):
                            self._mark_monster(row, col)
                            monsters += 1

            if monsters == 0:
                self.rotate()
            else:
                return monsters

            
    def _check_for_monster(self, row: int, col: int) -> bool:
        '''
        Returns True if a monster begins at a given # and False otherwise.
        '''
        try:
            if self._valid_char(row + 1, col + 1) and \
               self._valid_char(row + 1, col + 4) and \
               self._valid_char(row, col + 5) and \
               self._valid_char(row, col + 6) and \
               self._valid_char(row + 1, col + 7) and \
               self._valid_char(row + 1, col + 10) and \
               self._valid_char(row, col + 11) and \
               self._valid_char(row, col + 12) and \
               self._valid_char(row + 1, col + 13) and \
               self._valid_char(row + 1, col + 16) and \
               self._valid_char(row, col + 17) and \
               self._valid_char(row - 1, col + 18) and \
               self._valid_char(row, col + 18) and \
               self._valid_char(row, col + 19):
                return True
            else:
                return False

        except KeyError:
            return False
        
        except IndexError:
            return False


    def _mark_monster(self, row: int, col: int) -> None:
        '''Marks the monster with O's'''
        self._mark_char(row, col)
        self._mark_char(row + 1, col + 1)
        self._mark_char(row + 1, col + 4)
        self._mark_char(row, col + 5)
        self._mark_char(row, col + 6)
        self._mark_char(row + 1, col + 7)
        self._mark_char(row + 1, col + 10)
        self._mark_char(row, col + 11)
        self._mark_char(row, col + 12)
        self._mark_char(row + 1, col + 13)
        self._mark_char(row + 1, col + 16)
        self._mark_char(row, col + 17)
        self._mark_char(row - 1, col + 18)
        self._mark_char(row, col + 18)
        self._mark_char(row, col + 19)

    
    def _valid_char(self, row: int, col: int) -> bool:
        '''
        Returns True if the character at the given locattion is a #.
        Returns False otherwise.
        '''
        return self._image[row][col] == '#' or \
               self._image[row][col] == 'O'


    def _mark_char(self, row: int, col: int) -> None:
        '''Replaces the character at the given location with an O'''
        self._image[row][col] = 'O'

    
    def rotate(self) -> None:
        '''Rotates the image 90 degrees clockwise'''
        rotated = []
        for i in range(len(self._image)):
            rotated.append(reverse_list(self._get_col(i)))
        self._image = rotated

        
    def flip_vertical(self) -> None:
        '''Flips the image along the x-axis'''
        flipped = []
        for i in range(len(self._image) - 1, -1, -1):
            flipped.append(self._image[i])
        self._image = flipped


    def flip_horizontal(self) -> None:
        '''Flips the image along the y-axis'''
        flipped = []
        for i in range(len(self._image)):
            flipped.append(reverse_list(self._image[i]))
        self._image = flipped


    def _get_col(self, col: int) -> [[str]]:
        '''
        Returns a 2D list of characters representing a given column in the
        image.
        '''
        char_list = []
        for row in range(len(self._image)):
            char_list.append(self._image[row][col])
        return char_list
        
    
    def _strip_and_combine_tiles(self, board: [[Tile]]) -> [str]:
        '''
        Returns a list of strings representing the combined board with the
        borders of each tile removed.
        '''
        image = []
        size = board.get_size()
        for section in board.get_board():
            for row in range(1, 9):
                char_list = []
                for tile in section:
                    char_list += tile.get_img()[row][1:-1]
                image.append(char_list)
        return image


    def _listify_image(self, image: [[str]]) -> [[str]]:
        '''
        Returns the image with as a 2D list of characters instead of a list of
        strings.
        '''
        new_image = image

        for row in range(len(new_image)):
            stripped_line = new_image[row]
            char_list = [char for char in stripped_line]
            new_image[row] = char_list

        return new_image


    
