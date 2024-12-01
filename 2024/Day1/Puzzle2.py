import numpy as np

list1 = []
list2 = []

with open('Input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    first, second = line.split()
    list1.append(int(first))
    list2.append(int(second))

simScore = [i*list2.count(i) for i in list1]

print(sum(simScore))