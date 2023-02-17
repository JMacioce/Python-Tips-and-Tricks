a: int = 300
b: int = a * 1

print('a:', a)
print('b:', b)

# Test to see if a is not equal to be b because it checks for the same value
print(a != b)
# Test to see if a is not b because it checks for the actual instance
print(a is not b)

# Printing the id of each object to prove they are truly different
print('id(a):', id(a))
print('id(b):', id(b))
