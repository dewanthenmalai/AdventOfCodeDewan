import math
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input
from AdventOfCodeUtils.graph_module import modified_kruskal_3d, last_edge_kruskal_3d

is_test = True

def puzzle1(input):
    iters = 10 if is_test else 1000
    result = modified_kruskal_3d(input, iters)
    #print(sorted([len(s) for s in result.subsets()], reverse=True))
    #print(sorted([len(s) for s in result.subsets()], reverse=True)[:3])
    print(math.prod(sorted([len(s) for s in result.subsets()], reverse=True)[:3]))
    return

def puzzle2(input):
    last_edge = last_edge_kruskal_3d(input)
    if last_edge is None:
        print("Last edge is null!")
        return
    #print(f"Last edge between ({last_edge.v1.x},{last_edge.v1.y},{last_edge.v1.z}) and ({last_edge.v2.x},{last_edge.v2.y},{last_edge.v2.z})")
    print(last_edge.v1.x*last_edge.v2.x)
    return

def main():
    global is_test
    args = parse_arguments()
    is_test = args.test
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="line")
    

if __name__ == "__main__":
    main()
