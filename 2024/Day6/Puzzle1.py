DIRS = {
    'N': (0,-1),
    'S': (0,1),
    'E': (1,0),
    'W': (-1,0)
}

def index_2D(list, elem):
    retList = []
    for i, x in enumerate(list):
        for j in range(len(x)):
            if list[i][j] == elem:
                retList.append((j, i))
    return retList

def tuple_add(A,B):
    return tuple([a+b for a,b in zip(A,B)])

def tuple_get(list, tup):
    try:
        return list[tup[1]][tup[0]]
    except IndexError:
        return None

def rotate(dir, rot):
    right = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }
    left = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }
    match rot:
        case 'right': return right[dir]
        case 'left': return left[dir]
        case _: raise ValueError('Invalid rotation')

with open('Input.txt', 'r') as file:
    lines = file.readlines()

grid = [[c for c in line.rstrip()] for line in lines]
visited = set()
min = 0
max_x =len(grid[0])
max_y = len(grid)
obstacles = set(index_2D(grid, '#'))

temp = index_2D(grid, '^')
if len(temp) != 1:
    print('Could not find guard')
    print(temp)
    exit(1)

guardPos = temp[0]
guardDir = 'N'

while min <= guardPos[0] < max_x and min <= guardPos[1] < max_y:
    visited.add(guardPos)
    nextPos = tuple_add(guardPos, DIRS[guardDir])
    if nextPos in obstacles:
        guardDir = rotate(guardDir, 'right')
    else:
        guardPos = nextPos

print(len(visited))