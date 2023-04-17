a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

print(a==b)
print (a is b)
print()


b[-1].append(99)
print(a==b)
print (a is b)