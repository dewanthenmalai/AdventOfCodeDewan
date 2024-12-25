import re
from collections import defaultdict

def is_input(operand):
    return operand[0] in 'xy'

with open('Input.txt','r') as file:
    input = file.read()

initial_value_pattern = r'(\w{3}): ([0-1])'
rule_pattern = r'(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})'

initial_value_matches = re.finditer(initial_value_pattern, input)
rules = re.findall(rule_pattern, input)

max_z = sorted([r[3] for r in rules if r[3].startswith('z')])[-1]

use_map = defaultdict(list)
for r in rules:
    use_map[r[0]].append(r)
    use_map[r[2]].append(r)

swapped = set()
for r in rules:
    left, op, right, result = r
    # Special-case the first and last bits
    if result == max_z or 'x00' in {left,right}:
        continue
    
    if op == 'XOR':
        if is_input(left):
            if not is_input(right):
                swapped.add(result)
                print(r, 'only 1 is an input')
            if result[0] == 'z' and result != 'z00':
                swapped.add(result)
                print(r, 'output is a z when using an input')
            usage = use_map[result]
            using_ops = [o[1] for o in usage]
            if result != 'z00' and sorted(using_ops) != ['AND', 'XOR']:
                swapped.add(result)
                print(r, 'wrong output ops', usage)
        else:
            if result[0] != 'z':
                swapped.add(result)
                print(r, 'output was not a z')
    
    elif op == 'AND':
        if is_input(left):
            if not is_input(right):
                swapped.add(result)
                print(r, 'only 1 is an input')
        usage = use_map[result]
        if [o[1] for o in usage] != ['OR']:
            swapped.add(result)
            print(r, 'wrong usage', usage)
    
    elif op == 'OR':
        if is_input(left) or is_input(right):
            swapped.add(result)
            print(r, 'used an input')
        usage = use_map[result]
        using_ops = [o[1] for o in usage]
        if sorted(using_ops) != ['AND', 'XOR']:
            swapped.add(result)
            print(r, 'wrong usage', usage)
    
    else:
        print(r, 'unknown op')

print(len(swapped))
print(','.join(sorted(swapped)))