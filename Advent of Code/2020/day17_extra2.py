
from day17_extra1 import ConwayCube

class Universe:
    def __init__(self, center):
        self._center = center
        self._layers = dict()
        self._copy = self._make_copy()


    def count_active(self) -> int:
        '''Returns the number of active cubes in the dimension'''
        active = 0
        for z in self._layers:
            layer = self._layers[z]
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
        for z in self._layers:
            layer = self._layers[z]

            if self._count_active_in_layer(layer) > 0:
                print(f'\nz={z}')
                self._display_layer(layer)
    

    def _display_layer(self, layer: [[ConwayCube]]) -> None:
        '''Displays the cubes in a given layer'''
        for row in layer:
            for cube in row:
                print(cube.display(), end = '')
            print()
        print()


    def update(self) -> None:
        '''Updates the dimension based on certain rules'''        
        for z in self._layers:
            layer = self._layers[z]
            for row in range(len(layer)):
                for col in range(len(layer[row])):
                    cube = layer[row][col]
                    active_neighbors = self._check_neighbors(z, row, col)
                    # Active -> 2 or 3 neighbors Active -> Active
                    # Otherwise, change to Inactive
                    if cube.is_active():
                        if active_neighbors == 2 or \
                           active_neighbors == 3:
                            continue
                        else:
                            cube.deactivate()
                    # Inactive -> 3 neightbors Active -> Active
                    # Otherwise, remain Inactive 
                    else:
                        if active_neighbors == 3:
                            cube.activate()
                        else:
                            continue
        self._copy = self._make_copy()


    def _check_neighbors(self, z: int, row: int, col: int) -> int:
        '''Returns the number of active neighboring cubes'''
        active = 0

        active += self._check_layer(z, -1, row, col)
        active += self._check_layer(z, 0, row, col)
        active += self._check_layer(z, 1, row, col)

        return active



    def _check_layer(self, z: int, z_delta: int, row: int, col: int) -> int:
        '''Returns the number of active cubes on a local layer'''
        active = 0
        
        if z_delta != 0:
            if self._check_cube(z + z_delta, row, col):
                active += 1
                
        if self._check_cube(z + z_delta, row, col - 1):
            active += 1

        if self._check_cube(z + z_delta, row, col + 1):
            active += 1

        if self._check_cube(z + z_delta, row - 1, col):
            active += 1

        if self._check_cube(z + z_delta, row - 1, col - 1):
            active += 1

        if self._check_cube(z + z_delta, row - 1, col + 1):
            active += 1

        if self._check_cube(z + z_delta, row + 1, col):
            active += 1

        if self._check_cube(z + z_delta, row + 1, col - 1):
            active += 1

        if self._check_cube(z + z_delta, row + 1, col + 1):
            active += 1

        return active


    def _check_cube(self, z: int, row: int, col: int) -> bool:
        '''
        Returns True if the cube at this location is active.
        Returns False otherwise.
        '''
        if row < 0 or col < 0:
            return False
        
        try:
            return self._copy[z][row][col].is_active()

        except KeyError:
            return False

        except IndexError:
            return False


    def _make_copy(self) -> {int: [[ConwayCube]]}:
        '''Returns a copy of the dimension's layers'''
        layers = dict()

        for z in self._layers:
            layer = self._layers[z]
            new_layer = []
            for row in range(len(layer)):
                cubes = []
                for col in range(len(layer[row])):
                    cube = layer[row][col]
                    new_cube = ConwayCube(cube.is_active())
                    cubes.append(new_cube)
                new_layer.append(cubes)
            layers[z] = new_layer

        return layers
                

    def expand(self, cycles: int) -> None:
        '''Expands the dimension to hold future cubes'''
        layer_count = cycles
        row_count = 2 * cycles + len(self._center)
        col_count = 2 * cycles + len(self._center[0])

        # Add blank layers
        for i in range(1, layer_count + 1):
            self._layers[i] = self._empty_layer(row_count, col_count)
            self._layers[-i] = self._empty_layer(row_count, col_count)

        self._expand_center_layer(row_count, col_count, cycles)
        self._copy = self._make_copy()


    def _expand_center_layer(self, rows: int, cols: int, delta: int) -> None:
        '''Expands the center layer to the given dimensions'''
        center = self._center
        new_layer = self._empty_layer(rows, cols)

        for row in range(len(center)):
            for col in range(len(center[row])):
                new_layer[row + delta][col + delta] = center[row][col]

        self._layers[0] = new_layer
        

    def _empty_layer(self, rows: int, cols: int) -> [[ConwayCube]]:
        '''Returns an 2D list of inactive cubes with the given dimensions.'''
        layer = []

        for row in range(rows):
            cubes = []
            for col in range(cols):
                cubes.append(ConwayCube())
            layer.append(cubes)

        return layer
