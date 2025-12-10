import itertools
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def get_corners(coords):
    sums = [p[0]+p[1] for p in coords]
    diffs = [p[0]-p[1] for p in coords]
    top_left = coords[sums.index(min(sums))]
    bottom_right = coords[sums.index(max(sums))]
    top_right = coords[diffs.index(min(diffs))]
    bottom_left = coords[diffs.index(min(diffs))]
    return [top_left, bottom_left, top_right, bottom_right]

def get_area(c1, c2):
    return (abs(c1[0]-c2[0])+1) * (abs(c1[1]-c2[1])+1)

def Sutherland_Hodgman(i, c, min_x, max_x, min_y, max_y, coords):
    x,y = c
    in_x = min_x + 1 <= x < max_x
    in_y = min_y + 1 <= y < max_y
    nx,ny = coords[(i+1) % len(coords)]
    match (in_x,in_y):
        case (True, True):
            return False
        case (True, False):
            if x == nx:
                lo, hi = sorted((y, ny))
                if min_y != max_y and (min_y in range(lo, hi + 1)) and (max_y in range(lo, hi + 1)):
                    return False
            return True
        case (False,True):
            if y == ny:
                lo, hi = sorted((x, nx))
                if min_x != max_x and (min_x in range(lo, hi + 1)) and (max_x in range(lo, hi + 1)):
                    return False
            return True
        case (False,False):
            return True

def puzzle1(input):
    coords = [[int(i) for i in l.split(",")] for l in input]
    corners = get_corners(coords)
    areas = [get_area(c1,c2) for c1,c2 in itertools.combinations(corners,2)]
    #print(areas)
    print(max(areas))
    return

def puzzle2(input):
    coords = [[int(i) for i in l.split(",")] for l in input][::-1]
    max_area = 0
    points = [[0,0],[0,0]]
    for c1,c2 in itertools.combinations(coords,2):
        min_x, max_x = sorted((c1[0],c2[0]))
        min_y, max_y = sorted((c1[1],c2[1]))
        if all(Sutherland_Hodgman(i,c,min_x,max_x,min_y,max_y,coords) for i,c in enumerate(coords)):
            max_area = max(max_area, get_area(c1,c2))
    print(max_area)
    return

def main():
    args = parse_arguments()
    is_test = args.test
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="line")
    

if __name__ == "__main__":
    main()
