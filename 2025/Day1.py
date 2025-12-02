from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def puzzle1(input):
    dial = 50
    passcode = 0
    signed_input = [int(line[1:]) * (1 if line[0] == "R" else -1) for line in input]
    for instr in signed_input:
        dial = (dial + instr) % 100
        if dial == 0:
            passcode += 1
    print(f"Passcode is {passcode}")
    return

def puzzle2(input):
    dial = 50
    passcode = 0
    signed_input = [int(line[1:]) * (1 if line[0] == "R" else -1) for line in input]
    for instr in signed_input:
        if instr > 0:
            if dial + instr >= 100:
                passcode += (dial + instr) // 100
        elif dial != 0:
            if dial + instr <= 0:
                passcode += 1 + abs(dial + instr) // 100
        elif instr <= -100:
            passcode += abs(instr) // 100
        dial = (dial + instr) % 100
    print(f"Passcode is {passcode}")
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="line")
    

if __name__ == "__main__":
    main()