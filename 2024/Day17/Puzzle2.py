import copy
import re

with open('Input.txt','r') as file:
    input = file.read()

pattern = r'Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([0-9](,[0-9])*)'
match = re.compile(pattern).match(input)
reg_A,reg_B,reg_C,inst = match.groups()[:4]

inst = [int(c) for c in inst.split(',')]
registers = {
    'A': int(reg_A),
    'B': int(reg_B),
    'C': int(reg_C)
}

def combo_operand(op, reg):
    match op:
        case 0 | 1 | 2 | 3:
            return op
        case 4:
            return reg['A']
        case 5:
            return reg['B']
        case 6:
            return reg['C']
        case 7:
            print('7 is not a valid combo operand')
            exit(1)
        case _:
            raise ValueError(f'Unknown operand {op}')

def run_program(program, registers):
    output = []
    inst_ptr = 0
    while inst_ptr < len(inst):
        opcode = inst[inst_ptr]
        operand = inst[inst_ptr+1]
        match opcode:
            case 0:
                registers['A'] = registers['A'] >> combo_operand(operand, registers)
            case 1:
                registers['B'] = registers['B'] ^ operand
            case 2:
                registers['B'] = combo_operand(operand, registers) % 8
            case 3:
                if registers['A'] != 0:
                    inst_ptr = operand
                    continue
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                output.append(combo_operand(operand,registers) % 8)
            case 6:
                registers['B'] = registers['A'] >> combo_operand(operand, registers)
            case 7:
                registers['C'] = registers['A'] >> combo_operand(operand, registers)
        inst_ptr += 2
    return output

def run_a_value(program, registers, a):
    reg = copy.copy(registers)
    reg['A'] = a
    return run_program(program,reg)

queue = list(range(8))
while queue:
    possible_a = queue.pop(0)
    if (possible_a.bit_length()//3) + 1 == len(inst):
        print(possible_a)
        exit(0)
    for i in range(8):
        a = (possible_a << 3) + i
        if run_a_value(inst,registers,a) == inst[-((a.bit_length()//3)+1):]:
            queue.append(a)
print('Failed to find value')
exit(1)