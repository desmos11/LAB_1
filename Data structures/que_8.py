names = ["Alice", "Charlie", "Bob", "shankar", "OM", "Muskanhero", "muskan", "bhaiya", "ram"]
name_count = {}
for name in set(names):  # Using set() to avoid duplicate counting
    name_count[name] = names.count(name)
print(name_count)