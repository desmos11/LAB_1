import random

l=[]
l_1=[]
for i in range(10):
    l.append(random.randint(1,101))

for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            l.pop(i)

print(l)
