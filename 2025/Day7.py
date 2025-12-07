from collections import defaultdict
from  AdventOfCodeUtils import grid_module
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def puzzle1(input):
    beams = set()
    splits = 0
    start_list = grid_module.get_locations(input, "S")
    if len(start_list) != 1:
        print(f"Invalid number of start points: {start_list}")
        return
    start = start_list[0]
    beams.add(start[0])
    for row in input:
        splitters = [i for i,x in enumerate(row) if x == "^"]
        for b in beams.copy():
            if b in splitters:
                beams.remove(b)
                beams.update([b-1,b+1])
                splits += 1
    #print(sorted(beams))
    print(splits)
    return

def puzzle2(input):
    timelines = defaultdict(int)
    start_list = grid_module.get_locations(input, "S")
    if len(start_list) != 1:
        print(f"Invalid number of start points: {start_list}")
        return
    start = start_list[0]
    timelines[start[0]] += 1
    for row in input:
        splitters = [i for i,x in enumerate(row) if x == "^"]
        existing_timelines = [t for t in timelines.keys() if timelines[t] > 0]
        for t in existing_timelines:
            if t in splitters:
                count = timelines[t]
                timelines[t] = 0
                timelines[t-1] += count
                timelines[t+1] += count
    print(sum(timelines.values()))
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="grid")
    

if __name__ == "__main__":
    main()
