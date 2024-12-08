from itertools import product, zip_longest

def test_calibration(test):
    total = test[0]
    num = [str(n) for n in test[1]]
    perms = list(product(['+','*'],repeat=len(num)-1))
    for p in perms:
        expr = ['('*len(p), num[0]]
        paren = [')' for i in range(len(p))]
        expr.extend([x for xs in zip(p,num[1:],paren) for x in xs])
        check_val = eval(''.join(expr))
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