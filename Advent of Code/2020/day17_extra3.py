
from day17_extra1 import ConwayCube

class Hyperverse:
    def __init__(self, center):
        self._center = center
        self._universes = dict()
        self._copy = self._make_copy()


    def count_active(self) -> int:
        '''Returns the number of active cubes in the hyperverse'''
        active = 0
        for w in self._universes:
            universe = self._universes[w]
            for z in universe:
                layer = universe[z]
                active += self._count_active_in_layer(layer)
        return active


    def _count_active_in_layer(self, layer: [[ConwayCube]]) -> int:
        '''Returns the number of active cubes in the layer'''
        active = 0
        for row in layer:
            for cube in row:
                if cube.is_active():
                    active += 1
        return active


    def display_layers(self) -> None:
        '''Displays every layer with an active cube'''
        for w in self._universes:
            universe = self._universes[w]
            for z in universe:
                layer = universe[z]
                if self._count_active_in_layer(layer) > 0:
                    print(f'\nz={z}, w={w}')
                    self._display_layer(layer)


    def _display_layer(self, layer: [[ConwayCube]]) -> None:
        '''Displays the cubes in a given layer'''
        for row in layer:
            for cube in row:
                print(cube.display(), end = '')
            print()
        print()


    def update(self) -> None:
        '''Updates the hyperverse based on certain rules'''
        for w in self._universes:
            universe = self._universes[w]
            for z in universe:
                layer = universe[z]
                for row in range(len(layer)):
                    for col in range(len(layer[row])):
                        cube = layer[row][col]
                        active_neighbors = self._check_neighbors(w, z, row, col)
                        if cube.is_active():
                            if active_neighbors == 2 or \
                               active_neighbors == 3:
                                continue
                            else:
                                cube.deactivate()
                        else:
                            if active_neighbors == 3:
                                cube.activate()
                            else:
                                continue
        self._copy = self._make_copy()


    def _check_neighbors(self, w: int, z: int, row: int, col: int) -> int:
        '''Returns the number of active neighboring cubes'''
        active = 0

        active += self._check_universe(w, -1, z, row, col)
        active += self._check_universe(w, 0, z, row, col)
        active += self._check_universe(w, 1, z, row, col)

        return active


    def _check_universe(self, w: int, w_delta: int, z: int, row: int, col: int) -> int:
        '''Returns the number of active cubes in a local universe'''
        active = 0

        active += self._check_layer(w, z, row, col, (w_delta, -1))
        active += self._check_layer(w, z, row, col, (w_delta, 0))
        active += self._check_layer(w, z, row, col, (w_delta, 1))

        return active


    def _check_layer(self, w: int, z: int, row: int, col: int, delta: (int, int)) -> int:
        '''Returns the number of active cubes on a local layer'''
        active = 0
        w_delta, z_delta = delta

        if w_delta != 0 or z_delta != 0:
            if self._check_cube(w + w_delta, z + z_delta, row, col):
                active += 1
                
        if self._check_cube(w + w_delta, z + z_delta, row, col - 1):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row, col + 1):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row - 1, col):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row - 1, col - 1):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row - 1, col + 1):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row + 1, col):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row + 1, col - 1):
            active += 1

        if self._check_cube(w + w_delta, z + z_delta, row + 1, col + 1):
            active += 1

        return active


    def _check_cube(self, w: int, z: int, row: int, col: int) -> bool:
        '''
        Returns True if the cube at this location is active.
        Returns False otherwise.
        '''
        if row < 0 or col < 0:
            return False
        
        try:
            return self._copy[w][z][row][col].is_active()

        except KeyError:
            return False

        except IndexError:
            return False


    def _make_copy(self) -> {int: {int: [[ConwayCube]]}}:
        '''Returns a copy of the hyperverse'''
        universes = dict()

        for w in self._universes:
            universe = self._universes[w]
            new_universe = dict()
            for z in universe:
                layer = universe[z]
                new_layer = []
                for row in range(len(layer)):
                    cubes = []
                    for col in range(len(layer[row])):
                        cube = layer[row][col]
                        new_cube = ConwayCube(cube.is_active())
                        cubes.append(new_cube)
                    new_layer.append(cubes)
                new_universe[z] = new_layer
            universes[w] = new_universe

        return universes
        


    def expand(self, cycles: int) -> None:
        '''Expands the hyperverse to hold future cubes'''
        universe_count = cycles
        layer_count = cycles + 1
        row_count = 2 * cycles + len(self._center)
        col_count = 2 * cycles + len(self._center)

        # Add empty universes
        for i in range(universe_count + 1):                
            self._universes[i] = self._empty_universe(
                layer_count, row_count, col_count)
            self._universes[-i] = self._empty_universe(
                layer_count, row_count, col_count)

        self._expand_center(row_count, col_count, cycles)
        self._copy = self._make_copy()


    def _expand_center(self, rows: int, cols: int, delta: int) -> None:
        '''Expands the center layer to the given dimensions'''
        center = self._center
        new_layer = self._empty_layer(rows, cols)

        for row in range(len(center)):
            for col in range(len(center[row])):
                new_layer[row + delta][col + delta] = center[row][col]
        self._universes[0][0] = new_layer


    def _empty_universe(self, layers: int, rows: int, cols: int) -> {int: [[ConwayCube]]}:
        '''
        Returns a dictonary of 2D lists of inactive cubes with the given
        dimensions.
        '''
        universe = dict()

        for i in range(layers):
            universe[i] = self._empty_layer(rows, cols)
            universe[-i] = self._empty_layer(rows, cols)
        return universe

        
    def _empty_layer(self, rows: int, cols: int) -> [[ConwayCube]]:
        '''Returns an 2D list of inactive cubes with the given dimensions.'''
        layer = []

        for row in range(rows):
            cubes = []
            for col in range(cols):
                cubes.append(ConwayCube())
            layer.append(cubes)

        return layer
    
