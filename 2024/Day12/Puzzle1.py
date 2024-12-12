from tqdm import tqdm

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]

with open('Input.txt', 'r') as file:
    lines = file.readlines()

garden = [[c for c in line.rstrip()] for line in lines]

def tuple_add(a, b):
    return (a[0]+b[0],a[1]+b[1])

def tuple_get(grid, loc):
    if 0 <= loc[0] < len(garden[0]) and 0 <= loc[1] < len(garden):
        return garden[loc[1]][loc[0]]
    return None

def get_region(garden, loc):
    region = {loc}
    plant = tuple_get(garden, loc)
    next = [tuple_add(loc,dir) for dir in DIRS]
    i = 0
    while i < len(next):
        if next[i] not in region and tuple_get(garden, next[i]) == plant:
            region.add(next[i])
            next.extend([tuple_add(next[i],dir) for dir in DIRS])
        i += 1
    return region

def get_perimeter(region):
    total = 0
    for loc in region:
        total += sum([1 for dir in DIRS if tuple_add(loc,dir) not in region])
    return total
    
regions = []
checked = set()
for j, row in enumerate(garden):
    for i in range(len(row)):
        if (i,j) in checked:
            continue
        region = get_region(garden,(i,j))
        regions.append(region)
        checked |= region

price = 0
for region in tqdm(regions):
    area = len(region)
    perimeter = get_perimeter(region)
    price += area * perimeter

print(price)