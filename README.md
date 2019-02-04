# Game_Of_Life
An implementation of Conway's Game Of Life in Python, using matplotlib to animate the simulation. 
The game takes place on an initial grid of size 100x100 cells which expands every time a pixel near
the grid boundary comes to life to simulate an infinite grid. We therefore assume that the user is only
interested in seed grids which are smaller than or equal to 100x100 cells.

The required external libraries are listed in the requirements.txt (numpy and matplotlib).

# Using the simulation
To use the simulation, first run Game_Of_Life.py - a prompt will then appear asking the user to enter one of the
pre-made seed grids:

<p align="center">
<img src="https://github.com/scottgilmartin/Game_Of_Life/blob/master/Images/Screen%20Shot%202019-02-04%20at%2021.29.35.png" alt="alt text" width="60%" height="50%"></p>

