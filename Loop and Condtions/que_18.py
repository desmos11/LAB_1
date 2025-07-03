n = int(input("Enter a number: "))
str_n = str(n)
reversed_str = str_n[::-1]

if reversed_str == str_n:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")