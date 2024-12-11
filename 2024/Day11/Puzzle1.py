from tqdm import tqdm
from itertools import chain

def increment_stone(stone):
    if stone != 0:
        raise ValueError(f'Stone value is {stone}, value must be 0')
    return stone+1

def split_stone(stone):
    stone_str = str(stone)
    if len(stone_str)%2 != 0:
        raise ValueError(f'Stone length is {len(stone)}, length must be even')
    return int(stone_str[:(len(stone_str)//2)]), int(stone_str[(len(stone_str)//2):])

def multiply_stone(stone):
    return stone * 2024

def eval_stone(stone):
    if stone == 0:
        return increment_stone(stone)
    elif len(str(stone))%2 == 0:
        return split_stone(stone)
    return multiply_stone(stone)

with open('Input.txt','r') as file:
    line = file.read()

stones = [int(c) for c in line.rstrip().split()]

blinks = 25

for _ in tqdm(range(blinks)):
    stones = list(chain(*(i if isinstance(i,tuple) else (i,) for i in map(eval_stone, stones))))

print(len(stones))