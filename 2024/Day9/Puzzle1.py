with open('Input.txt', 'r') as file:
    line = file.read().rstrip()

map = [int(c) for c in line]
disk = []
fileDes = 0
for idx, val in enumerate(map):
    if idx % 2 == 0:
        disk += val * [str(fileDes)]
        fileDes += 1
    else:
        disk += val * ['.']

start = 0
end = len(disk)-1
while start < end:
    if disk[start] != '.':
        start += 1
        continue
    if disk[end] == '.':
        end -= 1
        continue
    disk[start] = disk[end]
    disk[end] = '.'

checksum = 0
for i, fileDes in enumerate(disk):
    if fileDes == '.':
        break
    checksum += i * int(fileDes)

print(checksum)