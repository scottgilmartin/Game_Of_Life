# Game Of Life
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

The user should type the seed of their choice and press enter. A matplotlib animation will then be generated showing the grid as it evolves with each time step. The animation will run until closed.

The pre-made seed grids are:

* An empty seed: which simply produces a grid which is empty at every time step.
* An oscillator: 3 live cells in a line which alternates between horizontal and vertical with each time step.
* A glider: A simple "glider", a shape which travels in the SE direction forever. The shape repeats every 4 time steps, displaced by one row and one column.
* A reverse_glider: As above, but travelling in the NW direction.
* A glider_gun: The Gosper glider gun - a seed which generates SE travelling gliders indefinitely.
* A random seed: Creates an initial grid in which the live cells are chosen at random within the given boundary.

# Examples

<p align="center">
<img src="https://github.com/scottgilmartin/Game_Of_Life/blob/master/Images/Screen%20Shot%202019-02-04%20at%2019.01.56.png" alt="alt text" width="40%" height="30%"></p>

<p align="center">
A screenshot of the Gosper glider gun after numerous timesteps. (test seed: glider_gun)</p>

<p align="center">
<img src="https://github.com/scottgilmartin/Game_Of_Life/blob/master/Images/Screen%20Shot%202019-02-03%20at%2015.03.08.png" alt="alt text" width="35%" height="30%"></p>

<p align="center">
A screenshot of a random seed after numerous timesteps. (test seed: random)</p>
