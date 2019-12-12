file = open('input.txt')
values = file.readline()
values = values.split(',')
items=[]
for value in values:
    items.append(int(value))
pos = 0
items[1] = 12
items[2] = 2
while True:
    if items[pos] == 1:
        items[items[pos+3]] = items[items[pos+1]]+items[items[pos+2]]
    elif items[pos] == 2:
        items[items[pos+3]] = items[items[pos+1]] * items[items[pos+2]]
    else:
        break
    pos += 4
print(items[0])