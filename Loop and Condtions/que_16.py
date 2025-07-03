l=[]
for i in range(0,10):
    w=int(input("Enter the number: "))
    l.append(w)

p=0
n=0
o=0
for i in range(0,10):
    if(l[i]>0):
        p+=1
    elif(l[i]<0):
        n+=1
    else:
        o+=1

print(f"The no of positive number is {p}\n the no of negative  number is {n} and zero is {o} ")