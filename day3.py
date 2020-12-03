import numpy as np
from functools import reduce

import matplotlib
import matplotlib.pyplot as plt


def printmap(w):
    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = (50, 50) # (w, h)

    fig, ax = plt.subplots()
    fig.tight_layout()
    im = ax.imshow(worldmap)

def createmap(arr):
    pic = []    
    for l in lines:
        pic.append([1.0 if pix == '#' else 0.0 for pix in list(l)])
        
    worldmap = np.array(pic)
    return worldmap

def smashed(pix):
    if pix == 1.0:
        return True
    return False

def downhill(worldmap, idelta, jdelta, track = False):
    n = len(worldmap)
    m = len(worldmap[0])
    i = 0
    j = 0
    running = True
    trees = 0
    
    while running:
        inext = i+idelta
        jnext = (j+jdelta) % m

        if inext < n:
            c = worldmap[inext][jnext]
            pixcol = 0.2

            if smashed(c):
                trees += 1
                pixcol = 0.7
            
            if track:
                worldmap[inext][jnext] = pixcol    
                
        else:
            running = False

        i = inext
        j = jnext
    
    return trees


with open("../input/d3.txt") as f:
    lines = [line.rstrip() for line in f]
    
worldmap = createmap(lines)

trees = [1] * 5
trees[0] = downhill(worldmap, 1, 3, False)
trees[1] = downhill(worldmap, 1, 1, False)
trees[2] = downhill(worldmap, 1, 5, False)
trees[3] = downhill(worldmap, 1, 7, False)
trees[4] = downhill(worldmap, 2, 1, False)

print(trees)
res = reduce(lambda x,y: x*y, trees)
print(res)