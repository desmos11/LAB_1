prime = []
for k in range(2, 51):
    count = 0
    for i in range(1, k+1):
        if(k % i == 0):
            count += 1
    if(count == 2):
        prime.append(k)
prime_set = set(prime)
print("Set of prime numbers less than 50: ", prime_set)


# Check if a number exists in the set
num = int(input("Enter a number to check: "))
if num in prime_set:
    print(num, "is a prime number less than 50.")
else:
    print(num, "is NOT a prime number less than 50.")
