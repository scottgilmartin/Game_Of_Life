import random

SEED_SIZE = 100
MID = int(SEED_SIZE / 2)

# -----------------------------------------TEST SEEDS----------------------------------------------------------

empty = []

underpop = [(MID, MID)]

outofbounds = [(1, 0), (1, 1), (1, 2), (3, 1), (2, 0)]

oscillator = [(MID, MID - 1), (MID, MID), (MID, MID + 1)]  # scenario 6

glider = [(MID, MID - 1), (MID, MID), (MID, MID + 1), (MID - 2, MID),
          (MID - 1, MID + 1)]  # a basic glider which travels SE

reverse_glider = [(MID, MID - 1), (MID, MID), (MID, MID + 1), (MID + 2, MID),
                  (MID + 1, MID - 1)]  # a basic glider which travels NW

random = [(random.randint(10, SEED_SIZE - 10), random.randint(10, SEED_SIZE - 10)) for _ in range(int((MID - 10) ** 2))]
# a randomized seed

glider_gun = [(0, 24), (1, 22), (1, 24), (2, 12), (2, 13), (2, 20), (2, 21), (2, 34), (2, 35), (3, 11),
              (3, 15), (3, 20), (3, 21), (3, 34), (3, 35), (4, 0), (4, 1), (4, 10), (4, 16), (4, 20),
              (4, 21), (5, 0), (5, 1), (5, 10), (5, 14), (5, 16), (5, 17), (5, 22), (5, 24), (6, 10),
              (6, 16), (6, 24), (7, 11), (7, 15), (8, 12), (8, 13)]  # Gosper glider gun
