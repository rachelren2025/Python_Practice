'''
Python Variables - Assign Multiple Values
'''

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
print("-----Many Values to Multiple Variables-----")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z + "\n")

print()

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
print("-----One Value to Multiple Variables-----")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print()

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
print("-----Unpack a Collection-----")
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)