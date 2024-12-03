import numpy as np

safe = 0

def valid(arr):
    diff = np.diff(arr)
    unique = np.unique(np.sign(diff))
    return (len(unique) == 1) and (unique[0] != 0) and (abs(diff.max()) <= 3) and (abs(diff.min()) <= 3)

with open('Input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    vals = [int(a) for a in line.split()]
    if valid(vals):
        safe += 1

print(safe)