from itertools import product, zip_longest

def evaluate_expression(numbers, ops):
    if len(numbers)-1 != len(ops):
        raise ValueError('Mismatched number and operator counts')
    arr = numbers[::-1]
    for op in ops:
        match op:
            case '+':
                result = arr.pop() + arr.pop()
            case '*':
                result = arr.pop() * arr.pop()
            case '||':
                result = int(str(arr.pop()) + str(arr.pop()))
            case _:
                raise ValueError(f'Unknown operator "{op}"')
        arr.append(result)
    if len(arr) != 1:
        raise ValueError('Mismatched number and operator counts')
    return arr[0]

def test_calibration(test):
    total = test[0]
    num = test[1]
    perms = list(product(['+','*', '||'],repeat=len(num)-1))
    for p in perms:
        check_val = evaluate_expression(num, p)
        if check_val == total:
            return True
    return False

def convert_line(line):
    tmp = line.split(':')
    total = int(tmp[0])
    numbers = [int(e) for e in tmp[1].split()]
    return (total, numbers)

with open('Input.txt', 'r') as file:
    lines = file.readlines()

tests = [convert_line(line.rstrip()) for line in lines]
valid = [elem[0] for elem in filter(test_calibration, tests)]
print(sum(valid))