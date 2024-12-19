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

def get_combinations_recursively(pattern, towels, cache=dict()):
    if pattern in cache.keys():
        return cache[pattern]
    count = 0
    for t in towels:
        if pattern == t:
            count += 1
            continue
        if pattern[:len(t)] == t:
            count += get_combinations_recursively(pattern[len(t):],towels, cache)
    cache[pattern] = count
    return count

print(sum(get_combinations_recursively(p,towels) for p in patterns))