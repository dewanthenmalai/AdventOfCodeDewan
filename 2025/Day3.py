from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def puzzle1(input):
    max_joltages = []
    for bank in input:
        int_bank = [int(c) for c in bank]
        first_num = max(int_bank[:-1])
        first_num_loc = int_bank.index(first_num)
        second_num = max(int_bank[first_num_loc+1:])
        joltage = 10*first_num + second_num
        max_joltages.append(joltage)
    #print(max_joltages)
    print(sum(max_joltages))
    return

def puzzle2(input):
    max_joltages = []
    for bank in input:
        batteries = []
        battery_locs = []
        int_bank = [int(c) for c in bank]
        batteries.insert(0, max(int_bank[:-11]))
        battery_locs.insert(0, int_bank.index(batteries[0]))
        for i in range(-10,0):
            batteries.insert(0, max(int_bank[battery_locs[0]+1:i]))
            battery_locs.insert(0, int_bank[battery_locs[0]+1:i].index(batteries[0])+battery_locs[0]+1)
        batteries.insert(0, max(int_bank[battery_locs[0]+1:]))
        max_joltages.append(int("".join([str(d) for d in batteries[::-1]])))
    #print(max_joltages)
    print(sum(max_joltages))
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="line")
    

if __name__ == "__main__":
    main()
