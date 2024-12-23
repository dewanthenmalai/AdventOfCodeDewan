import re
from itertools import filterfalse

def get_neighbors(v, edges):
    neighbors = set()
    links = filter(lambda x: comp in x, edges)
    for e in edges:
        if v in e:
            neighbors.add(list(filterfalse(lambda c: c == v, e))[0])
    return neighbors

def Bron_Kerbosch(R, P, X, output, edges):
    if len(P) == 0 and len(X) == 0:
        output.append(R)
    while len(P) > 0:
        v = list(P)[0]
        neighbors = get_neighbors(v, edges)
        Bron_Kerbosch(R|{v}, P&neighbors, X&neighbors, output, edges)
        P.remove(v)
        X.add(v)

with open('Input.txt','r') as file:
    input = file.read()

pattern = r'([a-zA-Z]*)-([a-zA-Z]*)'

raw_connections = [tuple(sorted(match.groups())) for match in re.finditer(pattern, input)]
nodes = {item for sub in raw_connections for item in sub}

max_cliques = []
Bron_Kerbosch(set(), nodes, set(), max_cliques, raw_connections)
soln = max(max_cliques, key=len)
print(','.join(sorted(soln)))