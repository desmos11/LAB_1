n=int(input("Enter a number"))

for i in range(2,n+1):
    if(n%i==0):
        break

if(i==n):
    print(f"The number is Prime: {n}")

else:
        print(f"The number is not Prime: {n}")

    