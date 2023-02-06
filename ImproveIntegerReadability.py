# Python reads these numbers the same as eachother
num1 = 1_000_000
num2 = 1000000

sum = num1 + num2
print("Two Million -->", sum)
# This is how to format the print statement to include seperation with a specific character
print("Two Million -->", f"{sum:,}")
print("Two Million -->", f"{sum:_}")
