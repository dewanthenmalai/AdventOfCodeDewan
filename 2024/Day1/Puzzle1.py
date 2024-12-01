import numpy as np

list1 = []
list2 = []

with open('Input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    first, second = line.split()
    list1.append(int(first))
    list2.append(int(second))

list1.sort()
list2.sort()
diff = np.subtract(list1, list2)
out = np.abs(diff)
print(sum(out))