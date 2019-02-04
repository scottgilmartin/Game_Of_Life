from GOLclass import GameOfLife
from config import SEED_SIZE
from config import empty, underpop, outofbounds, oscillator, glider, reverse_glider
import unittest


class Tests(unittest.TestCase):
    """
    Test various scenarios and seeds.
    """
        
    def test_empty(self):
        game = GameOfLife(empty, SEED_SIZE)
        game.draw_grid()
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([]), 'Empty seed remains empty (Scenario 5 test)')
        
    def test_underpop(self):
        game = GameOfLife(underpop, SEED_SIZE)
        game.draw_grid()
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([]), 'Cell dies due to underpopulation')

    def test_oscillator(self):
        game = GameOfLife(oscillator, SEED_SIZE)
        game.draw_grid()
        self.assertEqual(set(game.live_cells), set([(50, 50), (50, 49), (50, 51)]), 'Scenario 6 test')
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([(50, 50), (49, 50), (51, 50)]), 'Scenario 6 test')
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([(50, 50), (50, 49), (50, 51)]), 'Scenario 6 test')
        
    def test_glider(self):
        game = GameOfLife(glider, SEED_SIZE)
        game.draw_grid()
        init_glider = game.live_cells
        self.assertEqual(set(init_glider), set([(49, 51), (50, 51), (50, 50), (48, 50), (50, 49)]),
                         'the initial glider is drawn correctly')
        game.update_grid()
        game.update_grid()
        game.update_grid()
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([(x+1, y+1) for (x, y) in init_glider]),
                         'the initial glider is displaced by 1 row and 1 column after 4 iterations')
    
    def test_reverse_glider(self):
        game = GameOfLife(reverse_glider, SEED_SIZE)
        game.draw_grid()
        init_glider=game.live_cells
        self.assertEqual(set(init_glider), set([(50, 51), (50, 50), (52, 50), (51, 49), (50, 49)]),
                         'the initial glider is drawn correctly')
        game.update_grid()
        game.update_grid()
        game.update_grid()
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([(x-1, y-1) for (x, y) in init_glider]),
                         'the initial glider is displaced by 1 row and 1 column after 4 iterations')
        
    def test_out_of_bounds(self):
        game = GameOfLife(outofbounds, SEED_SIZE)
        game.draw_grid()
        self.assertEqual(set(game.live_cells), set([(1, 2), (3, 1), (2, 0), (1, 0),(1, 1)]),
                         'the initial glider is drawn correctly')
        game.update_grid()
        self.assertEqual(set(game.live_cells), set([(11, 10), (10, 11), (11, 11), (12, 10), (12, 12)]),
                         'grid expands and glider redrawn correctly')


if __name__ == '__main__':
    unittest.main()
