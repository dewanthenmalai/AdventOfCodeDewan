import numpy as np
import matplotlib.pyplot as plt
from HailHelper import Stone

input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
lines = input.split('\n')
stones = [Stone(line) for line in lines]
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

datasets = [{'x': [(s.vel[0]*t)+s.pos[0] for t in np.linspace(0, 7, 700)], 'y': [(s.vel[1]*t)+s.pos[1] for t in np.linspace(0, 7, 700)], 'z': [(s.vel[2]*t)+s.pos[2] for t in np.linspace(0, 7, 700)], 'c': "red"} for s in stones]

for d in datasets:
    ax.plot(d['x'], d['y'], d['z'], color=d['c'])

ax.plot([(-3*t)+24 for t in np.linspace(0, 7, 700)], [(1*t)+13 for t in np.linspace(0, 7, 700)], [(2*t)+10 for t in np.linspace(0, 7, 700)], color="blue")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()

#3
#20
#24
