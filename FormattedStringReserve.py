text = "WOW"

print(f'{text}')
#print line with fill of character to the left
print(f'{text:%<20}')
#print line with fill of character to the right
print(f'{text:+>20}')
#print line with fill of character on both sides
print(f'{text:.^20}')
