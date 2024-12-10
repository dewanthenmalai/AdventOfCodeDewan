from itertools import groupby

def write_list(list, start, len, value):
    for i in range(start,start+len):
        list[i] = value

def find_free_block(disk, _len):
    for i,c in enumerate(disk):
        if c == '.':
            size = 0
            j = i
            while  j < len(disk) and disk[j] == '.':
                size += 1
                j += 1
            if size >= _len:
                return i
    return None
            

with open('Input.txt', 'r') as file:
    line = file.read().rstrip()

map = [int(c) for c in line]
disk = []
file_len = {}
fileDes = 0
for idx, val in enumerate(map):
    if idx % 2 == 0:
        disk += val * [str(fileDes)]
        file_len[fileDes] = val
        fileDes += 1
    else:
        disk += val * ['.']

#a = [0] * 10
#write_list(a,2,3,1)
#print(a)

sorted = dict(sorted(file_len.items(),reverse=True))
for id,size in sorted.items():
    loc = find_free_block(disk,size)
    file_loc = disk.index(str(id))
    if loc is None:
        continue
    elif loc < file_loc:
        write_list(disk,loc,size,str(id))
        write_list(disk,file_loc,size,'.')

checksum = 0
for i, fileDes in enumerate(disk):
    if fileDes == '.':
        continue
    checksum += i * int(fileDes)

print(checksum)