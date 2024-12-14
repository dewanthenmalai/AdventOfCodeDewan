import numpy as np
import re
from tqdm import tqdm

with open('Input.txt', 'r') as file:
    input = file.read()

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)\n"

tokens = []
for match in re.finditer(pattern,input):
    a_x,a_y,b_x,b_y,p_x,p_y = (int(i) for i in match.groups())
    p_x += 10000000000000
    p_y += 10000000000000
    b = (a_y * p_x - a_x * p_y) / (b_x * a_y - a_x * b_y)
    t = 0
    if b.is_integer():
        a = (p_x - b * b_x) / a_x
        if a.is_integer():
            t = 3*a + b
    tokens.append(int(t))

print(sum(tokens))