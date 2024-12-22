def calculate_secret(seed, iter, cache):
    current = seed
    for _ in range(iter):
        if current in cache.keys():
            current = cache[current]
        else:
            int_1 = (((current<<6)^current)%16777216)
            int_2 = (((int_1>>5)^int_1)%16777216)
            next = (((int_2<<11)^int_2)%16777216)
            cache[current] = next
            current = next
    return current

with open('Input.txt','r') as file:
    input = file.readlines()

seeds = [int(line.rstrip()) for line in input]

_cache = dict()
result = [calculate_secret(s,2000,_cache) for s in seeds]
print(sum(result))