import re

def apply_op(op, in1, in2):
    match op:
        case 'AND':
            return in1 and in2
        case 'OR':
            return in1 or in2
        case 'XOR':
            return in1 ^ in2
        case _:
            raise ValueError(f'Unknown operation "{op}"')

with open('Input.txt','r') as file:
    input = file.read()

initial_value_pattern = r'(\w{3}): ([0-1])'
rule_pattern = r'(\w{3}) (AND|OR|XOR) (\w{3}) -> (\w{3})'

initial_value_matches = re.finditer(initial_value_pattern, input)
rules = re.findall(rule_pattern, input)
wires = {m.group(1): int(m.group(2)) for m in initial_value_matches}

while len(rules) > 0:
    rule = rules.pop(0)
    if rule[0] in wires and rule[2] in wires:
        wires[rule[3]] = apply_op(rule[1], wires[rule[0]], wires[rule[2]])
    else:
        rules.append(rule)

output_wires = {k: v for k,v in wires.items() if k.startswith('z')}
output_digits = [i[1] for i in sorted(output_wires.items(),reverse=True)]
output_num = int(''.join(map(str,output_digits)),2)
print(output_num)