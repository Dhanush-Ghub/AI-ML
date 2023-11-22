f = open('text.txt','r')
lines=0
character=0
words=0
for i in f:
    lines+=1
    count=i.split()
    words=words+len(count)
    character=character+len(i)
print(lines)
print(words)
print(character)