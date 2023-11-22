with open('text1.txt', 'r') as f:
    list1 = [line.split() for line in f]

list2 = []

for line in list1:
    line = sorted(line) 
    line = [word for word in line ] 
    print(' '.join(line))

list2.sort()

with open('text.txt', 'w') as f:
    for line in list2:
        f.write(line + '\n')

