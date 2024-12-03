import re

regex = r"(do|don't)\(\)|(mul)\((\d*),(\d*)\)"

with open('Input.txt', 'r') as file:
    lines = file.readlines()

total = 0

flag = 1
for line in lines:
    matches = re.findall(regex, line)
    for m in matches:
        match m[0]:
            case "do":
                flag = 1
            case "don't":
                flag = 0
            case _:
                total += int(m[2])*int(m[3])*flag

print(total)