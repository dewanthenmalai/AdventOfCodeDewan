import re

class SpringSet:
    def __init__(self, springs, counts):
        self.springs = springs
        self.counts = counts
    
    def checkArrangement(self, arr):
        return [len(m) for m in re.findall(r"#+",arr)] == self.counts
    
    def checkPartialMatch(self, arr):
        matches = list(re.finditer(r"#+",arr))
        matchLens = [len(m) for m in re.findall(r"#+",arr)]
        unknowns = list(re.finditer(r"\?+",arr))
        left = False
        right = False
        middle = False
        if len(unknowns) == 0:
            return self.checkArrangement(arr)
        if min([i.start() for i in unknowns]) < min([i.start() for i in matches]):
            i = min([len(matches), len(self.counts)])
            left = all([matchLens[i] <= self.counts[i] for i in range(i)])
        if max([i.start() for i in unknowns]) < max([i.start() for i in matches]):
            i = min([len(matches), len(self.counts)])
            right = all([matchLens[::-1][i] <= self.counts[::-1][i] for i in range(i)])
        if any(i.start() in range(matches[0].start(),matches[-1].start()) for i in unknowns):
            i = min([len(matches), len(self.counts)])//2
            middle = all([matchLens[i] < self.counts[i] for i in range(i,-i,-1)])
        return left or right or middle
    
    def evaluateSprings(self,arr=None):
        if arr == None:
            return self.evaluateSprings(self.springs)
        i = arr.find('?')
        cDot = 0
        cHash = 0
        if i == -1:
            return 1*self.checkArrangement(arr)
        dotStr = arr[:i]+'.'+arr[i+1:]
        if self.checkPartialMatch(dotStr):
            cDot = self.evaluateSprings(dotStr)
        hashStr = arr[:i]+'#'+arr[i+1:]
        if self.checkPartialMatch(hashStr):
            cHash = self.evaluateSprings(hashStr)
        return cDot + cHash