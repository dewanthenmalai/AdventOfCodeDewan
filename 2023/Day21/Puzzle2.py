#so the adjacency matrix attempt doesn't really scale that well, so I switched to an iterative approach with memoization
import numpy as np
#import matplotlib.pyplot as plt
from collections import defaultdict

def tupAdd(a, b):
    return (a[0]+b[0],a[1]+b[1])

def valid(coord, shape):
    return 0 <= coord[0] < shape[0] and 0 <= coord[1] < shape[1]

def get(grid, coord):
    if valid(coord, grid.shape):
        return grid[coord]
    return '\0'

#this method gives us an "infinite" grid by using modular arithmetic to loop coordinates
def loopGet(grid, coord):
    actual = (coord[0]%grid.shape[0], coord[1]%grid.shape[1])
    return get(grid, actual)

def step(grid, coord, count, maxDepth, stepDepths=defaultdict(list), cache=defaultdict(bool)):
    key = (coord, count)
    if cache[key]: return
    steps = defaultdict(tuple)
    nexts = [tupAdd(coord, d) for d in dirs]
    for c in nexts:
        validStep = loopGet(grid, c) in ".S"
        steps[c] = validStep
        if validStep:
            stepDepths[count].append(c)
    cache[key] = True
    if count == maxDepth: return
    
    for c in nexts:
        if steps[c]:
            step(grid, c, count+1, maxDepth, stepDepths, cache)
    

file = open("Input.txt", 'r')
input = file.read()

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
steps = 350

grid = np.asarray([[c for c in l] for l in input.split('\n')])
w = np.where(grid == 'S')
start = (w[0][0], w[1][0])

stepDepths = defaultdict(list)
step(grid, start, 1, steps, stepDepths, defaultdict(bool))

#The first step is to inspect the input and see that it has a diamond pattern in such a way that it always takes exactly 65 steps to reach the edge of the diamond. In addition, the quarter diamonds in each corner are a section of the original diamond. That means it always takes 65 steps from the start to reach the edge of the diamond.

#if we plot the graph of step depth vs path length up to we can see that this function grows quadratically
#plt.plot(stepDepths.keys(), [len(s) for s in stepDepths.values()])
#plt.show()

#from here, we can derive the formula for the quadratic from three sample points: y(0), y(1), and y(2)
#this is done by noticing that the quadractic formula, ax^2+bx+c is linear in [a,b,c]
#this means that we can get [a,b,c] by solving the matrix equation [[0,0,1],[1,1,1],[4,2,1]]*[a,b,c] = [y(0),y(1),y(2)]
#we can "pre-solve" this by finding the inverse of the above matrix: 1/2[[1,-2,1],[-3,4,-1],[2,0,0]]

#since 26501365 is exactly 65 more than a multiple of 3, we can "condense" the quadratic, so the y values we use will be the step count at the boundary of each successive grid: 65, 196, and 327, treating them as 0, 1, and 2
#this means we only have to simulate up to 327 steps for the answer -> I simulate a bit further as a "buffer" of sorts
#once we get the formula, all that remains is to calculate the "condensed" x value at 26501365, which is (26501365-65)/131

y0 = len(set(stepDepths[65]))
y1 = len(set(stepDepths[196]))
y2 = len(set(stepDepths[327]))

a = (y0-2*y1+y2)/2
b = (-3*y0+4*y1-y2)/2
c = y0
n = (26501365-65)/131

paths = (a*(n**2)) + (b*n) + c
print(int(paths))