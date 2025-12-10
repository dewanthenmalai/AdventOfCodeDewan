import re
import ast
import numpy as np
from collections import deque
from scipy.optimize import Bounds, LinearConstraint, milp
from AdventOfCodeUtils.args_module import parse_arguments
from AdventOfCodeUtils.input_module import parse_input

def parse_machine(line):
    pattern = r"\[([\.#]*)\] ((?:\(\d+(?:,\d+)*\) )*){(\d+(?:,\d+)*)}"
    m = re.match(pattern, line)
    lights = m.group(1)
    buttons = [ast.literal_eval(b) for b in m.group(2).replace("(","[").replace(")","]").split()]
    joltages = [int(j) for j in m.group(3).split(",")]
    return (lights,buttons,joltages)

def generate_tree_with_bfs(root_value, search_value, buttons):
    class Node:
        def __init__(self, value, depth):
            self.value = value
            self.depth = depth
            self.children = []
        
        def generate_children(self):
            for b in buttons:
                child_value = list(self.value)
                for l in b:
                    match child_value[l]:
                        case "#":
                            child_value[l] = "."
                        case ".":
                            child_value[l] = "#"
                child_node = Node("".join(child_value), self.depth+1)
                self.children.append(child_node)
    
    root = Node(root_value, 0)
    queue = deque([root])
    while queue:
        current_node = queue.popleft()
        current_node.generate_children()
        queue.extend(current_node.children)
        for child in current_node.children:
            if child.value == search_value:
                return child.value, child.depth

def solve_ilp(joltages, buttons):
    A = np.zeros((len(joltages),len(buttons)))
    for j, idx in enumerate(buttons):
        for i in idx:
            A[i,j] = 1
    
    b = np.array(joltages)
    c = np.ones(len(buttons))
    
    constraints = LinearConstraint(A, b, b)
    integrality = np.ones(len(buttons))
    bounds = Bounds(lb=0, ub=np.inf)
    
    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
    
    if not res.success:
        print(f"Failed to find solution for joltages {joltages}: {res.message}")
        return -1
    
    solution = np.round(res.x).astype(int)
    
    if not np.all(A @ solution == b):
        print(f"Solutiuon {solution} is invalid for joltages {joltages}")
        return -1
    
    return int(np.sum(solution))

def puzzle1(input):
    machines = [parse_machine(l) for l in input]
    machine_presses = []
    for m in machines:
        start_val = list("." * len(m[0]))
        search_value, total_presses = generate_tree_with_bfs(start_val, m[0], m[1])
        machine_presses.append(total_presses)
    #print(machine_presses)
    print(sum(machine_presses))
    return

def puzzle2(input):
    machines = [parse_machine(l) for l in input]
    machine_presses = []
    for m in machines:
        total_presses = solve_ilp(m[2], m[1])
        machine_presses.append(total_presses)
    #print(machine_presses)
    print(sum(machine_presses))
    return

def main():
    args = parse_arguments()
    parse_input(puzzle1, puzzle2, puzzle=args.puzzle, test=args.test, style="line")
    

if __name__ == "__main__":
    main()
