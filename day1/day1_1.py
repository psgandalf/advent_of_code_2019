file = open('input.txt')
rows = file.readlines()
sum = 0
for row in rows:
    value = int(row.strip())
    value = value // 3 - 2
    sum += value
print(sum)
    