from itertools import product

def tupSub(a,b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

class Block:
    def __init__(self, init):
        self.end1, self.end2 = [[int(c) for c in b.split(',')] for b in init.split('~')]
        self.floor = min(self.end1[2], self.end2[2])
        self.height = abs(self.end1[2]-self.end2[2])
        self.support = []
        self.supporting = []
    
    def __str__(self):
        return f"{self.end1}->{self.end2}"
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if type(other) is Block:
            return self.end1 == other.end1 and self.end2 == other.end2
        return False
    
    def __lt__(self, other):
        return self.floor < other.floor
    
    def __gt__(self, other):
        return self.floor > other.floor