'''
Python has a set of built-in methods that you can use on strings.
For more visit: https://www.w3schools.com/python/python_ref_string.asp
'''
print("\n=============Upper Case=============")
print("The upper() method returns the string in upper case:")
a = "Hello, World!"
print('Original:', a)
print(a.upper())

print("\n=============Lower Case=============")
print("The lower() method returns the string in lower case:")
a = "Hello, World!"
print('Original:', a)
print(a.lower())

print("\n=============Remove Whitespace=============")
print('Whitespace is the space before and/or after the actual text, and very often you want to remove this space.')
print('The strip() method removes any whitespace from the beginning or the end:\n')
a = " Hello, World! "
print('Original:', a)
print(a.strip()) # returns "Hello, World!"

print("\n=============Replace String=============")
print('The replace() method replaces a string with another string:')
a = "Hello, World!"
print('Original:', a)
print(a.replace("H", "J"))

print("\n=============Split String=============")
print('The split() method returns a list where the text between the specified separator becomes the list items.')
print('The split() method splits the string into substrings if it finds instances of the separator:\n')
a = "Hello, World!"
print('Original:', a)
print(a.split(",")) # returns ['Hello', ' World!']

print("\nexample for fun")
b = "today was the night before christmas. tmrw is the day of christmas. yesterday was two days before christmas"
print(b)
print(b.split(' '))