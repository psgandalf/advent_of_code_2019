file = open('input.txt')
rows = file.readlines()
sum = 0
for row in rows:
    value = int(row.strip())
    value = value // 3 - 2
    sum += value
    while True:
        fuel_value = value // 3 - 2
        if fuel_value > 0:
            sum += fuel_value
            value = fuel_value
        else:
            break
    
print(sum)
    