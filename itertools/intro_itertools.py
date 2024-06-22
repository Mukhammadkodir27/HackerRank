r = range(1, 10)
i = iter(r)

print(next(i))
print(next(i))
for x in i:
    print(x)
