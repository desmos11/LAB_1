string = input("Enter a string: ")
d = {}
for i in string:
    if i not in d.keys():
        d[i] = string.count(i)
print("Character count in the string is: ", d)
