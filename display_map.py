# display_map.py
# Print out basic text representation of a map
# to do: assign variables representing map features 
# randomly select variables to fill a 5x5 square

import random

tree = "T"
water = "~"
path = "="
monster = "!"
wall = "I"

i = 1
while i < 6:
    tile = random.randint(1, 5)
    if tile == 1: 
        print(tree)
    elif tile == 2: 
        print(water)
    elif tile == 3: 
        print(path)
    elif tile == 4:
        print(monster)
    elif tile == 5:
        print(wall)
    else:
        print("error")
    i += 1
    
