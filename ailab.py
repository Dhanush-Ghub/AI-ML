f = open('text.txt','r')
f1=open('text1.txt','r')
list1=[]
list2=[]
list3=[]
list1 = [line.split() for line in f]
list2 = [line.split() for line in f1]

for i in list1:
    for j in list2:
            common_words = [word for word in i if word in j]
            if common_words:
                 list3.append(common_words)
print(list3)
len1=len(list1)
len2=len(list2)
total_words=len1+len2

similarity_index=len(list3)/total_words
print(similarity_index)