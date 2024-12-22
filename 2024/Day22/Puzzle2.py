from collections import defaultdict

def calculate_secret(seed, iter, cache, lookup):
    current = seed
    prev_price = current % 10
    change = (prev_price,)
    first = set()
    for _ in range(iter):
        if current in cache.keys():
            current = cache[current]
        else:
            int_1 = (((current<<6)^current)%16777216)
            int_2 = (((int_1>>5)^int_1)%16777216)
            next = (((int_2<<11)^int_2)%16777216)
            cache[current] = next
            current = next
        last_price = current % 10
        if len(change) > 3:
            change = change[1:] + (last_price-prev_price,)
            if change not in first:
                lookup[change].append(last_price)
                first.add(change)
        else:
            change += (last_price-prev_price,)
        prev_price = last_price
    return current

with open('Input.txt','r') as file:
    input = file.readlines()

seeds = [int(line.rstrip()) for line in input]

_cache = dict()
_lookups = defaultdict(list)
sequences = [calculate_secret(s,2000,_cache,_lookups) for s in seeds]
print(max(sum(n) for n in _lookups.values()))