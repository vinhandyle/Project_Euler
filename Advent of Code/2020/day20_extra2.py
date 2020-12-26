
from day20_extra0 import *
from day20_extra1 import Tile

import math

CHEAT = False

class Jigsaw:
    def __init__(self, tiles: [Tile]):
        self._tiles = tiles
        self._size = math.sqrt(len(tiles))
        self._init_board()


    def get_size(self) -> int:
        '''Returns the size of the board'''
        return int(self._size)

    
    def get_tiles(self) -> [Tile]:
        '''Returns a list of the board's tiles'''
        return self._tiles


    def get_board(self) -> [[Tile]]:
        '''Returns the board'''
        return self._board

    
    def _init_board(self) -> None:
        '''Initializes the board'''
        self._board = []
        section = []
        for i in range(len(self._tiles)):
            section.append(self._tiles[i])
            if (i + 1) % self._size == 0:
                self._board.append(section)
                section = []

    
    def display_board(self) -> None:
        '''Displays the board'''
        for section in self._board:
            for row in range(10):
                for tile in section:
                    print(tile.get_img()[row], end = ' ')
                print()
            print()


    def display_board_ids(self) -> None:
        '''Displays the IDs of each tile on the board'''
        size = int(self._size)
        for row in range(size):
            for col in range(size):
                print(self._board[row][col].get_id(), end = ' ')
            print()


    def product_of_corners(self) -> int:
        '''Returns the product of the corner tiles' IDs'''
        if CHEAT:
            total = 1

            for tile in self._tiles:
                if tile.get_type() == 'corner':
                    total *= tile.get_id()

            return total

        else:
            end = int(self._size - 1)
            return self._board[0][0].get_id() * \
                   self._board[0][end].get_id() * \
                   self._board[end][0].get_id() * \
                   self._board[end][end].get_id()


    def swap_tiles(self, pos1: (int, int), pos2: (int, int)) -> None:
        '''Swaps the positions of two tiles in the board'''
        x1, y1 = pos1
        x2, y2 = pos2
        tile1 = self._board[x1][y1]
        tile2 = self._board[x2][y2]
        self._board[x1][y1] = tile2
        self._board[x2][y2] = tile1

        
    def arrange_by_type(self) -> None:
        '''
        Rearranges the tiles such that:
        Tiles with two matches move to the corners,
        Tiles with three matches move to the edges, and
        Tile with four matches move to the center.
        Whether the tiles match with their surroundings is irrelevant.
        '''
        self._type_check_tiles()
        corners = []
        edges = []
        centers = []

        for tile in self._tiles:
            type = tile.get_type()
            if type == 'corner':
                corners.append(tile)
            elif type == 'edge':
                edges.append(tile)
            else:
                centers.append(tile)

        self._corners = corners
        self._edges = edges
        self._centers = centers
        
        self._set_corners(corners)
        self._set_edges(edges)
        self._set_centers(centers)


    def _set_corners(self, corners: [Tile]) -> None:
        '''Places the corner tiles onto the board'''
        end = int(self._size - 1)
        self._board[0][0] = corners[0]
        self._board[0][end] = corners[1]
        self._board[end][0] = corners[2]
        self._board[end][end] = corners[3]


    def _set_edges(self, edges: [Tile]) -> None:
        '''Places the edge tiles onto the board'''
        index = 0
        end = int(self._size - 1)
        for i in range(1, end):
            self._board[0][i] = edges[index]
            index += 1

        for i in range(1, end):
            self._board[end][i] = edges[index]
            index += 1

        for i in range(1, end):
            self._board[i][0] = edges[index]
            index += 1

        for i in range(1, end):
            self._board[i][end] = edges[index]
            index += 1


    def _set_centers(self, centers: [Tile]) -> None:
        '''Places the center tiles onto the board'''
        index = 0
        end = int(self._size - 1)
        for row in range(1, end):
            for col in range(1, end):
                self._board[row][col] = centers[index]
                index += 1


    def _type_check_tiles(self) -> None:
        '''
        Checks how many sides of each tile is matchable and assigns the
        appropriate type to the tile.
        '''
        for tile in self._tiles:
            matching_sides = 0
            sides = tile.get_sides()
            for _tile in self._tiles:
                if tile.get_id() != _tile.get_id():
                    _sides = _tile.get_sides()
                    for side in sides:
                        for _side in _sides:
                            if can_match(side, _side):
                                matching_sides += 1

            tile.set_type(matching_sides)
            
    
    def complete(self) -> None:
        '''Rotates, flips, and rearranges the tiles until they all fit'''
        self._configure_corners()
        self._configure_edges()
        self._configure_centers()


    def _configure_corners(self) -> None:
        '''
        Rotates and flips the corner tiles so that their matchable sides are
        facing inwards.
        '''
        end = int(self._size - 1)
        self._handle_corner((0, 0))
        self._handle_corner((0, end))
        self._handle_corner((end, 0))
        self._handle_corner((end, end))


    def _handle_corner(self, position: (int, int)) -> None:
        '''
        Rotates and flips a corner tile so that their matchable sides are facing
        inwards
        '''
        row, col = position
        tile = self._board[row][col]

        # Save directional matching checks
        target_h = None
        target_v = None
        if row > 0:
            target_h = tile.get_top
        else:
            target_h = tile.get_bottom

        if col > 0:
            target_v = tile.get_left
        else:
            target_v = tile.get_right

        # Get matchable sides
        matchable = []
        sides = tile.get_sides()

        for _tile in self._tiles:
            if tile.get_id() != _tile.get_id():
                _sides = _tile.get_sides()
                for side in sides:
                    for _side in _sides:
                        if can_match(side, _side) and \
                           not side in matchable:
                            matchable.append(side)

        # Rotate until matchables are facing inwards
        complete = lambda side1, side2: (can_match(side1, target_h()) and \
                                         can_match(side2, target_v())) or \
                                         (can_match(side1, target_v()) and \
                                          can_match(side2, target_h()))

        while not complete(matchable[0], matchable[1]):
            tile.rotate_counter_clockwise()


    def _configure_edges(self) -> None:
        '''
        Rotates, flips, and rearranges the edge tiles so that they match with
        the corner tiles and their adjacent edge tiles.
        '''
        end = int(self._size - 1)
        self._handle_edges((0, 0), (0, 1))
        self._handle_edges((0, 0), (1, 0))
        self._handle_edges((0, end), (1, 0))
        self._handle_edges((end, 0), (0, 1))
        

    def _handle_edges(self, start: (int, int), delta: (int, int)) -> None:
        row, col = start
        d_r, d_c = delta
        end = int(self._size - 1)
        
        # Start from one corner then add edges that match
        target_dir = None
        if delta == (1, 0):
            target_dir = Tile.get_bottom
        else:
            target_dir = Tile.get_right

        target_side = target_dir(self._board[row][col])
        for i in range(1, end):
            new_row = row + i * d_r
            new_col = col + i * d_c
            new_pos = (new_row, new_col)
            
            self._find_matching_edge(target_side, new_pos)
            self._handle_edge(target_side, new_pos)
            target_side = target_dir(self._board[new_row][new_col])
            
        # If the next corner doesn't fit with this chain,
        # swap it with another corner until it does fit.
        new_row = row + end * d_r
        new_col = col + end * d_c
        new_pos = (new_row, new_col)
        self._swap_corner_to_match(new_pos, target_side)
                
        # Rotate and flip the corner until its matchable sides face inwards
        # and it lines up with the chain of edge tiles.
        self._fit_corner(new_pos, target_side)


    def _find_matching_edge(self, target_side: str, pos: (int, int)) -> None:
        '''
        Finds an edge tile that has an edge which matches the target side and
        places it in the given location on the board.
        '''
        row, col = pos
        matching_tile = None
        for tile in self._edges:
            if not tile.matched() and \
               matching_tile == None:
                sides = tile.get_sides()
                for side in sides:
                    if can_match(side, target_side):
                        tile.set_matching()
                        matching_tile = tile
                        break
        self._board[row][col] = matching_tile
        return matching_tile


    def _handle_edge(self, target_side: str, pos: (int, int)) -> None:
        '''
        Rotates and flips a tile in a given location of the board so that it
        lines up with the target side and its other sides face inwards.
        '''
        row, col = pos
        tile = self._board[row][col]
        end = int(self._size - 1)

        # Save the final direction of the matching side
        target_dir = None
        target_opp_dir = None
        mirror_target = None
        mirror_border = None

        if 0 < row < end:
            target_dir = tile.get_top
            target_opp_dir = tile.get_bottom
            mirror_target = tile.flip_vertical
            mirror_border = tile.flip_horizontal
            
        elif 0 < col < end:
            target_dir = tile.get_left
            target_opp_dir = tile.get_right
            mirror_target = tile.flip_horizontal
            mirror_border = tile.flip_vertical            

        # Save the final direction of the border side
        border_dir = None
        border_opp_dir = None

        if row == 0:
            border_dir = tile.get_top
            border_opp_dir = tile.get_bottom
        elif row == end:
            border_dir = tile.get_bottom
            border_opp_dir = tile.get_top
        elif col == 0:
            border_dir = tile.get_left
            border_opp_dir = tile.get_right
        elif col == end:
            border_dir = tile.get_right
            border_opp_dir = tile.get_left

        # Label the tile sides
        border_side, border_opp = self._find_border_side(tile)

        # Get the sides into their final position
        while not can_match(target_side, target_dir()) or \
              not can_match(border_side, border_dir()):            
            if can_match(target_side, target_opp_dir()):
                mirror_target()
            
            elif can_match(border_side, border_opp_dir()):
                mirror_border()

            else:
                tile.rotate_counter_clockwise()


    def _find_border_side(self, tile: Tile) -> (str, str):
        '''
        Given a tile, returns a tuple containing its border side and the side
        opposite of that.
        '''
        top = tile.get_top
        bottom = tile.get_bottom
        left = tile.get_left
        right = tile.get_right

        def opposite_side(side: 'function') -> 'function':
            if side == top:
                return bottom
            elif side == bottom:
                return top
            elif side == left:
                return right
            elif side == right:
                return left

        sides = [top, bottom, left, right]

        for side in sides:
            border = True
            for _tile in self._tiles:
                if border:
                    if tile.get_id() != _tile.get_id():
                        _sides = _tile.get_sides()
                        for _side in _sides:
                            if can_match(side(), _side):
                                border = False
                                break
            if border:
                return side(), opposite_side(side)


    def _swap_corner_to_match(self, corner_pos: (int, int), target_side: str) -> None:
        '''
        Swaps the given corner tile with another corner tile so that it matches
        with the target side.
        '''
        matched_corner = None
        for tile in self._corners:
            if matched_corner == None:
                sides = tile.get_sides()
                for side in sides:
                    if can_match(side, target_side):
                        matched_corner = tile
                        break

        matched_pos = (0, 0)
        for row in range(int(self._size)):
            if matched_pos == (0, 0):
                for col in range(int(self._size)):
                    if self._board[row][col] == matched_corner:
                        matched_pos = (row, col)
                        break

        self.swap_tiles(corner_pos, matched_pos)
                    

    def _fit_corner(self, corner_pos: (int, int), target_side: int) -> None:
        '''
        Rotates and flips the corner tile in the given location so that it lines
        up with the edge tiles.
        '''
        row, col = corner_pos
        tile = self._board[row][col]
        end = int(self._size - 1)
        self._handle_corner(corner_pos)

        matching_side = None
        if row == end:
            matching_side = tile.get_bottom
        elif col == end:
            matching_side = tile.get_left

        if not can_match(target_side, matching_side()):
            if corner_pos == (end, end):
                tile.rotate_counter_clockwise()
            else:
                tile.rotate_clockwise()
            tile.flip_vertical()
        
    
    def _configure_centers(self) -> None:
        '''
        Rotates, flips, and rearranges the center tiles so that they match with
        the edge tiles and their surrounding center tiles.
        '''
        end = int(self._size - 1)
        for row in range(1, end):
            for col in range(1, end):
                self._handle_center(row, col)


    def _handle_center(self, row: int, col: int) -> None:
        '''
        Finds a center tile which has sides that match the sides above and to the
        left of the given location and places it there. Then, rotates and flips
        the tile until it lines up with its surrounding tiles.
        '''
        match_above = self._board[row - 1][col].get_bottom()
        match_left = self._board[row][col - 1].get_right()

        tile = None
        for center in self._centers:
            if not center.matched() and \
               tile == None:
                sides = center.get_sides()
                for side in sides:
                    if can_match(side, match_above):
                        tile = center
                        tile.set_matching()
                        break

        self._board[row][col] = tile

        while not can_match(tile.get_top(), match_above):
            tile.rotate_clockwise()

        if tile.get_left() != match_left:
            tile.flip_horizontal()

    


    
