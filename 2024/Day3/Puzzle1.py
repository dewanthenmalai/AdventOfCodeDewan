import re

regex = r"mul\((\d*),(\d*)\)"

with open('Input.txt', 'r') as file:
    lines = file.readlines()

total = 0

for line in lines:
    matches = re.findall(regex, line)
    total += sum([int(m[0])*int(m[1]) for m in matches])

print(total)