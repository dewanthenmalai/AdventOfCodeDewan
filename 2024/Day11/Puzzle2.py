from tqdm import tqdm
from collections import defaultdict

with open('Input.txt','r') as file:
    line = file.read()

stones = line.rstrip().split()
stone_counts = defaultdict(int,{s:1 for s in stones})

blinks = 75

for _ in tqdm(range(blinks)):
    new_stone_counts = defaultdict(int)
    for stone, count in stone_counts.items():
        if stone == '0':
            new_stone_counts['1'] += count
        elif len(stone)%2 == 0:
            left = str(int(stone[:(len(stone)//2)]))
            right = str(int(stone[(len(stone)//2):]))
            new_stone_counts[left] += count
            new_stone_counts[right] += count
        else:
            new_stone_counts[str(int(stone)*2024)] += count
    stone_counts = new_stone_counts

print(sum(stone_counts.values()))