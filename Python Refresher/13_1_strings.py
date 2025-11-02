'''
Python Strings
Slicing Strings
Modify Strings
Concatenate Strings
Format Strings
Escape Characters
String Methods
String Exercises
'''

############## Python Strings ###################
print('############## Python Strings ###################')

print("=========Quotes inside Quotes=========")
'''
You can use a quote inside a string as long aa they dont match the quotes surrounding the string
'''
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

print("\n=========Strings Are Arrays=========")
'''
Strings in Python are arrays of unicode characters.
Python does not have a character data type, a single character is a string with a length of 1.
Square brackets can be used to access elements of the string
'''
print("Get the character at position 1 (remember that the first character has the position 0)")
a = "Hello, World!"
print(a[1])

print("\n=========Looping Through a String=========")
print('Since strings are arrays, we can loop through the characters in a string, with a for loop.')
for x in "banana":
  print(x)

print("\n=========String Length=========")
print('To get the length of a string, use the len() function.')
a = "Hello, World!"
print(len(a))

print("\n=========Check String=========")
'''To check if a certain phrase or character is present in a string, we can use the keyword in.'''
print('Check if "free" is present in the following text:')
txt = "The best things in life are free!"
print(txt)
print("free" in txt)

print("\nUse it in an if statement:")
txt = "The best things in life are free!"
print(txt)
if "free" in txt:
  print("Yes, 'free' is present.")

print("\n=========Check if NOT=========")
'''
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
'''
print('Check if "expensive" is NOT present in the following text:')
txt = "The best things in life are free!"
print(txt)
print("expensive" not in txt)