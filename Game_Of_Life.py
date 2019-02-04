from GOLclass import GameOfLife
from config import SEED_SIZE
from config import oscillator, glider, reverse_glider  # test seeds
from config import random, glider_gun, empty, underpop, outofbounds  # test seeds
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
Play the game of life with a specified test seed, implemented as a matplotlib animation. 
Run the code and enter (type in console) the name of one of the test seeds.
"""

choice = None

CHOICE_MAP = {'glider':glider, 'oscillator':oscillator, 'reverse_glider':reverse_glider,
              'random':random, 'glider_gun':glider_gun}

choice = input("To play, choose from one of the following seeds: glider, oscillator,"+
               "reverse_glider, glider_gun, or random: ")

if choice in CHOICE_MAP:
    
    seed_type = CHOICE_MAP[choice]
    game = GameOfLife(seed_type, SEED_SIZE) 
    game.draw_grid()
    
    fig, ax = plt.subplots()
    mat = ax.matshow(game.grid_mat, cmap='Greys_r')
    plt.axis('off')
    
    
    def update(data):  # update function for matplotlib animation
        game.update_grid()
        mat.set_data(game.grid_mat)
        return [mat]


    ani = animation.FuncAnimation(fig, update, interval=50, save_count=50, blit=True)
    
else:
        print('Choice not recognized')

