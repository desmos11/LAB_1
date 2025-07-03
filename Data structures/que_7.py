d1={'a': 900, 'b': 200, 'c': 300}
d2={'a': 300, 'b': 200, 'd': 400}
for k,v in d1.items():
    if k in d2:
        d2[k] += v
    else:
        d2[k] = v
print(d2)
print(d1)