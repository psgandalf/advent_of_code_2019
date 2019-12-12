file = open('input.txt')
values = file.readline()
values = values.split(',')
items1=[]
items=[]
for value in values:
    items1.append(int(value))
print(items1)
for noun in range(0, 100):
    #print(noun)
    items=items1
    for verb in range(0, 100):
        pos = 0
        items=items1
        #print(items1)
        items[1] = noun
        items[2] = verb
        print(items)
        #print(items1)
        while True:
            if items[pos] == 1:
                items[items[pos+3]] = items[items[pos+1]]+items[items[pos+2]]
            elif items[pos] == 2:
                items[items[pos+3]] = items[items[pos+1]] * items[items[pos+2]]
            else:
                break
            pos += 4
        #print(items[0])
        if items[0]==19690720:
            print(items[1]*100 + items[2])
            exit()