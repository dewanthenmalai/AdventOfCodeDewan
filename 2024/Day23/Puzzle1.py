import re
from itertools import combinations, filterfalse

with open('Input.txt','r') as file:
    input = file.read()

pattern = r'([a-zA-Z]*)-([a-zA-Z]*)'

raw_connections = [tuple(sorted(match.groups())) for match in re.finditer(pattern, input)]
nodes = {item for sub in raw_connections for item in sub}

trios = set()
for comp in filter(lambda c: c.startswith('t'), nodes):
    links = filter(lambda x: comp in x, raw_connections)
    for con1, con2 in combinations(links, 2):
        comp1 = list(filterfalse(lambda c: c == comp, con1))[0]
        comp2 = list(filterfalse(lambda c: c == comp, con2))[0]
        if tuple(sorted((comp1,comp2))) in raw_connections:
            trios.add(tuple(sorted((comp, comp1, comp2))))

print(len(trios))