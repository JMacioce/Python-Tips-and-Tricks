a: int = 800
b: int = a * 1

print('a:', a)
print('b:', b)

# False because a and b are the same value
print(a != b)
# True because a is not b because it checks for the actual instance
print(a is not b)

# Printing id of each object to prove they are truly different
print('id(a):', id(a))
print('id(b):', id(b))
