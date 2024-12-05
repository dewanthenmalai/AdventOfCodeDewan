import numpy as np

def tupAdd(a, b):
    return (a[0]+b[0],a[1]+b[1])

def valid(coord, shape):
    return 0 <= coord[0] < shape[0] and 0 <= coord[1] < shape[1]

def get(grid, coord):
    if valid(coord, grid.shape):
        return grid[coord]
    return '\0'

def adjListToMatrix(adjList, indices):
    adjMat = np.zeros((len(adjList), len(adjList)))
    for c, ns in adjList.items():
        for n in ns:
            adjMat[indices.index(c), indices.index(n)] = 1
    return adjMat

file = open("Input.txt", 'r')
input = file.read()

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
steps = 64

#overall goal is to convert the grid into an adjecency matrix
#from there we just need to take successive powers of the matrix, get the row that maps to our start, then get the count of nonzero values in that row
grid = np.asarray([[c for c in l] for l in input.split('\n')])
w = np.where(grid == 'S')
start = (w[0][0], w[1][0])
indices = [c for c,_ in np.ndenumerate(grid)]
adjList = {c: [tupAdd(c,dir) for dir in dirs if get(grid, tupAdd(c,dir)) in '.S'] for c,_ in np.ndenumerate(grid)}


adjMatrix = adjListToMatrix(adjList, indices)
afterSteps = np.linalg.matrix_power(adjMatrix, steps)
print(np.count_nonzero(afterSteps[indices.index(start)]))