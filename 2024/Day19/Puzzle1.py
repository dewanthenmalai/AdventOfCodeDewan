with open('Input.txt','r') as file:
    input = file.read()

towels = [t.strip() for t in input.split('\n\n')[0].split(',')]
patterns = [p.strip() for p in input.split('\n\n')[1].strip().split('\n')]

def check_pattern(pattern, towels, candidate = ""):
    for t in towels:
        test = candidate + t
        if test == pattern:
            return True
        if pattern.startswith(test):
            res = check_pattern(pattern, towels, test)
            if res:
                return True
    return False

for p in patterns:
    print(p)
    print(check_pattern(p,towels))
    print
# print(sum([check_pattern(p,towels) for p in patterns]))