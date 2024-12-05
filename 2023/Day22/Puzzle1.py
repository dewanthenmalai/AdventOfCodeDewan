from itertools import chain, product
from BlockHelper import Block

def projectDown(span, dist=1):
    return [tupSub(s, (0,0,dist)) for s in span]

def getDropLength(block, bricks):
    i = 0
    while True:
        i += 1
        projected = projectDown(block.getSpan(), i)
        if any([p[2] < 1 for p in projected]):
            break
        if any([p in set(chain(*[b.getSpan() for b in bricks if b != block])) for p in projected]):
            break
    return i-1

def canDrop(block, bricks):
    projected = projectDown(block.getSpan())
    if any([p[2] < 1 for p in projected]):
        return False
    occupied = set(chain(*[b.getSpan() for b in bricks if b != block]))
    return not any([p in occupied for p in projected])

file = open("Input.txt", 'r')
input = file.read()
lines = input.split('\n')

bricks = [Block(line) for line in lines]
bricks.sort(key=lambda x: x.floor)
#instead of dropping to zero floor, just make the lowest floor the lowest existing block
stableFloor = min(bricks).floor

stableBricks = []
for b in bricks:
    #check if brick is on floor
    if b.floor == stableFloor:
        stableBricks.append(b)
    else:
        support, supportLevel = [], 0
        #check if the current brick is on top of a stable brick
        for sb in stableBricks:
            if sb.end1[0] <= b.end2[0] and b.end1[0] <= sb.end2[0] and sb.end1[1] <= b.end2[1] and b.end1[1] <= sb.end2[1]:
                sbTop = sb.floor + sb.height
                if sbTop > supportLevel: support, supportLevel = [], sbTop
                if sbTop == supportLevel: support.append(sb)
        b.support = support
        b.floor = supportLevel + 1
        stableBricks.append(b)
        
        #take the bricks that support this one and add this one to their list of bricks they support
        for sb in support:
            sb.supporting.append(b)

canDisintegrate = []
for sb in stableBricks:
    if len(sb.supporting) > 0:
        #check that each brick that sb supports has other bricks supporting it
        if sum([1 for s in sb.supporting if len(s.support) > 1]) == len(sb.supporting):
            canDisintegrate.append(sb)
    else:
        #else sb doesn't support any bricks and can be freely disintegrated
        canDisintegrate.append(sb)

print(len(canDisintegrate))