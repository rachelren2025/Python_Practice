'''
Slicing--
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
print("============Slicing=============")
print("Get the characters from position 2 to position 5 (not included):")
b = "Hello, World!"
print(b)
print(b[2:5])

print("\n=============Slice From the Start=============")
'''
By leaving out the start index, the range will start at the first character:
'''
print('Get the characters from the start to position 5 (not included):')
b = "Hello, World!"
print(b)
print(b[:5])

print("\n=============Slice To the End=============")
'''
By leaving out the end index, the range will go to the end:
'''
print("Get the characters from position 2, and all the way to the end:")
b = "Hello, World!"
print(b)
print(b[2:])

print("\n=============Negative Indexing=============")
'''
Use negative indexes to start the slice from the end of the string:
'''
print('''
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
''')
b = "Hello, World!"
print(b)
print(b[-5:-2])