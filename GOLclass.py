import numpy
import copy


class GameOfLife:
    """
    Class containing the logic for an implementation of Conway's Game of Life.
    """

    neighbourhood = ((-1, -1), (-1,  0), (-1, +1),
                     ( 0, -1), (0,   0), ( 0, +1),
                     (+1, -1), (+1,  0), (+1, +1))
    
    def __init__(self, seed, size):
        """
        Initialize the grid for the given seed.
        """
        self.live_cells = seed  # list of coordinates of live cells in the grid
        self.pre_live_cells = seed  # list of coordinates of live cells in the grid of the previous iteration
        self.size = size
        self.grid_mat = numpy.zeros((self.size, self.size))
        self.live_nbs = [(x+n[0], y+n[1]) for (x, y) in self.live_cells for n in self.neighbourhood]
        # the set of cells that neighbour a live cell

    def draw_grid(self):
        """
        Convert the list of live cells into a matrix and plot it.
        """
        for cell in self.live_cells:
            self.grid_mat[int(cell[0]), int(cell[1])] = True
               
    def update_grid(self): 
        """
        Apply the Game of Life rules to the current grid.
        """  
        self.expand_grid()  # check if we need to expand the grid
        
        live_nbs = set([(x+n[0], y+n[1]) for (x, y) in self.live_cells for n in self.neighbourhood])
        
        new_grid = copy.deepcopy(self.grid_mat)
        new_live_cells = copy.deepcopy(self.live_cells)
        
        for cell in live_nbs:  # evaluate only the set of cells that neighbour a live cell
                  
            nbs = self.count_live_neighbours(cell[0], cell[1])
                
            if self.grid_mat[cell[0], cell[1]]:  # if the cell is alive
                    
                    if nbs < 2: 
                        new_grid[cell[0], cell[1]] = False  # underpopulation
                        new_live_cells.remove((cell[0], cell[1]))
                        
                    elif nbs > 3: 
                        new_grid[cell[0], cell[1]] = False  # overpopulation
                        new_live_cells.remove((cell[0], cell[1]))
                        
                    else:
                        pass  # survival
                        
            else:  # if the cell is dead
                if nbs == 3:
                    new_grid[cell[0], cell[1]] = True  # creation of life
                    new_live_cells.append((cell[0], cell[1]))
                    
                else:
                    pass  # no interactions
                        
        self.grid_mat = new_grid
        self.live_cells = new_live_cells
                         
    def expand_grid(self):
        """
        Expand the grid if a cell outside the current boundary becomes alive (simulate an infinite grid).
        """
        
        grid_x = [x[1] for x in self.live_cells]
        grid_y = [y[0] for y in self.live_cells]
        
        if len(grid_x) > 0 and len(grid_y) > 0:
            
            min_x = min(grid_x)
            min_y = min(grid_y)
            max_x = max(grid_x)
            max_y = max(grid_y)
              
            if min_x < 3 or min_y < 3 or max_x > self.size-3 or max_y > self.size-3:
                # check if a cell is alive near the grid boundary
                self.size = self.size+20
                self.grid_mat = numpy.zeros((self.size, self.size))
                self.live_cells = [(x+10, y+10) for (x, y) in self.live_cells]
                # get the coordinates of the live cells on the expanded grid
                self.draw_grid()
            
    def count_live_neighbours(self, x, y):
        """
        Counts the number of live cells in the 8 adjacent points around a point (x,y).
        """
        
        count =  (self.grid_mat[x-1, y-1] + self.grid_mat[x-1, y] + self.grid_mat[x-1, y+1] +
                  self.grid_mat[  x, y-1] +                         self.grid_mat[  x, y+1] +
                  self.grid_mat[x+1, y-1] + self.grid_mat[x+1, y] + self.grid_mat[x+1, y+1])

        return count
