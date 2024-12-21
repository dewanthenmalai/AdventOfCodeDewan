from Maps import NUM_SEQS, DIR_SEQS

def find_shortest(code, depth, cache):
    if depth == 0:
        return len(code)+1
    if code in cache[depth]:
        return cache[depth][code]
    full_code = 'A' + code + 'A'
    total = 0
    for i in range(len(full_code)-1):
        paths = DIR_SEQS[full_code[i]][full_code[i+1]]
        total += min([find_shortest(p,depth-1,cache) for p in paths])
    
    cache[depth][code] = total
    return total

with open('Input.txt','r') as file:
    input = file.readlines()

codes = [line.rstrip() for line in input]

cache = {i: dict() for i in range(1,26)}
sum = 0
for code in codes:
    full_code = 'A' + code
    total = 0
    for i in range(len(full_code)-1):
        paths = NUM_SEQS[full_code[i]][full_code[i+1]]
        total += min([find_shortest(p,25,cache) for p in paths])
    sum += total * int(code[:3])
print(sum)