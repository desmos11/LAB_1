l=[]
for i in range(4):
    w=int(input())
    l.append(w)

t=tuple(l)
print("\n")
print(f"The max among the tuple {t} is {max(t)}")
print(f"The min among the tuple {t} is {min(t)}")
