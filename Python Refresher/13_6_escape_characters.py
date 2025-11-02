'''
Escape Characters
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example:
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."

for more: https://www.w3schools.com/python/python_strings_escape.asp
'''

print("\n=============F-Strings=============")
print('To fix this problem, use the escape character \ before the double quote:')
txt = "We are the so-called \"Vikings\" from the north."
print(txt)