fruit_dict = {}
for _ in range(5):
    name = input("Enter fruit name: ")
    price = input("Enter price: ")
    fruit_dict[name] = price
search_key = input("\nWhich fruit's price do you want? ")
if search_key in fruit_dict:
    print(f"{search_key}'s price is {fruit_dict[search_key]}")
else:
    print("Sorry, this fruit isn't in our list.")
