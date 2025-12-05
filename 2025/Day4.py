import itertools
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input
from AdventOfCodeUtils import grid_module


def puzzle1(input):
    access = []
    for coord in itertools.product(range(len(input[0])), range(len(input))):
        if grid_module.get_pos(input,coord) != "@":
            continue
        adj = grid_module.get_adjacent(input,coord)
        rolls = [grid_module.get_pos(input,c) == "@" for c in adj]
        if sum(rolls) < 4:
            access.append(coord)
    for c in access:
        grid_module.set_pos(input,c,"x")
    #grid_module.grid_print(input)
    print(len(access))
    return

def puzzle2(input):
    total = 0
    while True:
        access = []
        for coord in itertools.product(range(len(input[0])), range(len(input))):
            if grid_module.get_pos(input,coord) != "@":
                continue
            adj = grid_module.get_adjacent(input,coord)
            rolls = [grid_module.get_pos(input,c) == "@" for c in adj]
            if sum(rolls) < 4:
                access.append(coord)
        for c in access:
            grid_module.set_pos(input,c,"x")
        total += len(access)
        if not len(access):
            break
    print(total)
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="grid")
    

if __name__ == "__main__":
    main()