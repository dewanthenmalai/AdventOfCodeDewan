with open('Input1.txt', 'r') as file:
    rule_text = file.readlines()

with open('Input2.txt', 'r') as file:
    update_text = file.readlines()

rules = [[int(c) for c in r.split('|')] for r in rule_text]
updates = [[int(c) for c in u.split(',')] for u in update_text]

total = 0
for update in updates:
    valid = True
    for rule in rules:
        if rule[0] not in update or rule[1] not in update:
            continue
        if update.index(rule[0]) >= update.index(rule[1]):
            valid = False
    if valid:
        total += update[(len(update)-1)//2]

print(total)