import types
import re
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

DIVISORS = [[],[],[1],[1],[1,2],[1],[1,2,3],[1],[1,2,4],[1,3],[1,2,5]]

def puzzle1(input):
    converted_input = [types.SimpleNamespace(start=int(i.split("-")[0]), end=int(i.split("-")[1])) for i in input]
    invalid_IDs = []
    for rng in converted_input:
        for id in range(rng.start, rng.end+1):
            id_str = str(id)
            if len(id_str)%2 == 1:
                continue
            mid = int(len(id_str) / 2)
            if id_str[:mid] == id_str[mid:]:
                invalid_IDs.append(id)
    #print(invalid_IDs)
    print(sum(invalid_IDs))
    return

def puzzle2(input):
    converted_input = [types.SimpleNamespace(start=int(i.split("-")[0]), end=int(i.split("-")[1])) for i in input]
    invalid_IDs = []
    for rng in converted_input:
        for id in range(rng.start, rng.end+1):
            id_str = str(id)
            match = re.match(r"^(.*)\1+$", id_str)
            if match:
                invalid_IDs.append(id)
    #print(invalid_IDs)
    print(sum(invalid_IDs))
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="list")
    

if __name__ == "__main__":
    main()
