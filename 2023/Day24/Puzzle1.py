import numpy as np
from itertools import combinations
from HailHelper import Stone

file = open("Input.txt", 'r')
input = file.read()
lines = input.split('\n')

lowerBound = 200000000000000
upperBound = 400000000000000

stones = [Stone(line) for line in lines]

#we can get intersections of paths by writing the their line equations in terms of x and y alone. This gives us a matrix equation we can solve
#if we define the parameteric equations for the path as x = m*t + b and y = n*t + c, the line equation is (1/m)*x - (1/n)*y = (b/m) - (c/n)
validCollisions = 0
for c in combinations(stones, 2):
    matrix = np.array([[(1/c[0].vel[0]), -(1/c[0].vel[1])], [(1/c[1].vel[0]), -(1/c[1].vel[1])]])
    inHomo = np.array([((c[0].pos[0]/c[0].vel[0]) - (c[0].pos[1]/c[0].vel[1])), ((c[1].pos[0]/c[1].vel[0]) - (c[1].pos[1]/c[1].vel[1]))])
    
    #uninvertible matrices have no inverses
    if np.linalg.det(matrix) == 0: continue
    
    solutionMat = np.linalg.inv(matrix)
    collision = solutionMat.dot(inHomo)
    #we need to quickly check that the collision happens for positive time for both stones
    t0 = (collision[0]-c[0].pos[0])/c[0].vel[0]
    t1 = (collision[0]-c[1].pos[0])/c[1].vel[0]
    
    if lowerBound < collision[0] < upperBound and lowerBound < collision[1] < upperBound and t0 > 0 and t1 > 0:
        validCollisions += 1

print(validCollisions)