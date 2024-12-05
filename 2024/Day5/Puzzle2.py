with open('Input1.txt', 'r') as file:
    rule_text = file.readlines()

with open('Input2.txt', 'r') as file:
    update_text = file.readlines()

rules = [[int(c) for c in r.split('|')] for r in rule_text]
updates = [[int(c) for c in u.split(',')] for u in update_text]

def check_order(rules, update):
    i = 0
    corrected = False
    while i < len(update)-1:
        current = update[i]
        next = update[i+1]
        
        if [next, current] in rules:
            update[i] = next
            update[i+1] = current
            corrected = True
            i = 0
        else:
            i += 1
    
    return update[(len(update)-1)//2] if corrected else 0

total = 0
for update in updates:
    total += check_order(rules, update)

print(total)