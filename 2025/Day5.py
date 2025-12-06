from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def between(val, start, end):
    return val >= start and val <= end

def puzzle1(input):
    raw_ranges, raw_ingredients = input.split("\n\n")
    str_ranges = raw_ranges.strip().split("\n")
    ranges = [[int(rng.split("-")[0]), int(rng.split("-")[1])] for rng in str_ranges]
    ingredients = [int(i) for i in raw_ingredients.strip().split("\n")]
    fresh = [any([between(i, rng[0], rng[1]) for rng in ranges]) for i in ingredients]
    #print(fresh)
    print(sum(fresh))
    return

def puzzle2(input):
    raw_ranges, raw_ingredients = input.split("\n\n")
    str_ranges = raw_ranges.strip().split("\n")
    ranges = [[int(rng.split("-")[0]), int(rng.split("-")[1])] for rng in str_ranges]
    ranges.sort(key=lambda i: i[0])
    merged_ranges = []
    for cur_start, cur_end in ranges:
        if not merged_ranges or cur_start > merged_ranges[-1][1]:
            merged_ranges.append([cur_start, cur_end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], cur_end)
    total_covered = 0
    for start, end in merged_ranges:
        total_covered += (end-start)+1
    print(total_covered)
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="none")
    

if __name__ == "__main__":
    main()
