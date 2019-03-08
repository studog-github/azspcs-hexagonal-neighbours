#
# Provides the hexgrid class
#
# Coordinates chosen to provide a "point-up" grid
#

class hexgrid:
    # Direction vectors
    NORTH_EAST = 0
    EAST = 1
    SOUTH_EAST = 2
    SOUTH_WEST = 3
    WEST = 4
    NORTH_WEST = 5
    DVECTORS = ()

    def __init__(self):
        self.resetGrid()

    def resetGrid(self):
        self.order = 0
        self.grid = []
        self.sum = 0
        self.valid = False

    def fromOrder(self, order):
        if (order < 0):
            return False
        self.order = order
        self.grid = []
        row_len = order
        row_inc = 1
        middle_row = order - 1
        for row in xrange(2 * order - 1):
            self.grid.append([1] * row_len)
            if (row == middle_row):
                row_inc = -1
            row_len += row_inc
        self.sum = 3 * order * order - 3 * order + 1
        self.valid = True
        return True

    def fromGrid(self, grid):
        if (grid is None or len(grid) == 0):
            return False
        order = len(grid[0])
        num_rows = 2 * order - 1
        if (len(grid) != num_rows):
            return False
        new_grid = []
        grid_sum = 0
        row_len = order
        row_inc = 1
        middle_row = order - 1
        for row in xrange(num_rows):
            if (len(grid[row]) != row_len):
                return False
            for i in grid[row]:
                if (type(i) != int):
                    return False
                elif (i < 1 or i > 7):
                    return False
                grid_sum += i
            new_grid.append(list(grid[row]))
            if (row == middle_row):
                row_inc = -1
            row_len += row_inc
        self.grid = new_grid
        self.order = order
        self.sum = grid_sum
        # Can't determine validity during parsing above because some neighbours are in the next
        # yet-to-be-parsed row
        self.valid = self.validate()

    def validate(self):
        pass

    def __repr__(self):
        return '{0}.{1}({2})'.format(self.__module__, self.__class__.__name__, self.grid)

    def __str__(self):
        return str(self.grid)
