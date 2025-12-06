import math
import re
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def puzzle1(input):
    parsed_input = [l.split() for l in input]
    problems = [list(row) for row in zip(*parsed_input)]
    solutions = []
    for p in problems:
        match p[-1]:
            case "+":
                solutions.append(sum([int(i) for i in p[:-1]]))
            case "*":
                solutions.append(math.prod([int(i) for i in p[:-1]]))
            case _:
                print(f"Unknown operator {p[-1]}")
    #print(solutions)
    print(sum(solutions))
    return

def puzzle2(input):
    lines = input.split("\n")
    numbers = lines[:-1]
    operators = lines[-1:][0].split()
    rotated_list = [list(row) for row in zip(*numbers)]
    rotated = "\n".join(["".join(row) for row in rotated_list])
    raw_number_sets = re.split(r"\n\s*\n", rotated)
    number_sets = [s.split() for s in raw_number_sets]
    solutions = []
    for set, op in zip(number_sets, operators):
        match op:
            case "+":
                solutions.append(sum([int(i) for i in set]))
            case "*":
                solutions.append(math.prod([int(i) for i in set]))
            case _:
                print(f"Unknown operator {op}")
    #print(solutions)
    print(sum(solutions))
    return

def main():
    args = parse_arguments()
    parse_style = "line" if args.puzzle == 1 else "none"
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style=parse_style)
    

if __name__ == "__main__":
    main()
