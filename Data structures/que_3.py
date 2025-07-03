l= []
for i in range(10):
    x = int(input("Enter a number: "))
    l.append(x)


print(l)
even_list= []
for i in l:
    if (i%2 == 0):
        even_list.append(i)
print("Even numbers in the list are: ", even_list)