'''
Python Operators

Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:
'''
print("\n=============Python Operators=============")
print(10+5)

print('''
Although the + operator is often used to add together two values, 
like in the example above, it can also be used to add together a 
variable and a value, or two variables:
''')
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
print(sum1)
print(sum2)
print(sum3)

'''
Arithmetic operators
Assignment operators
    - +=
    - -=
    - *=
    - /=    division, returns a float
    - %=
    - //=   floor division, returns an integer
    - **=
Comparison operators
Logical operators
    - and
    - or 
    - not: reverse the result, returns False if the result is True
Identity operators
    - is: returns True if both variables are the same object
        - ex: x is y
    - is not: returns True if both variables are not the same object
        - ex: x is not y
Membership operators
    - in: returns True if a sequence with the specified value is present in the object
        - ex: x in y
    - not in: returns True if a sequence with the specified value is not present in the
        - ex: x not in y
Bitwise operators
    - &   AND
        - The & operator compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.
    - |   OR
        - The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
    - ^   XOR
        - The | operator compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1. If both bits are 0, the corresponding result bit is set to 0.
    - ~   NOT
        - The ~ operator is a unary operator that performs bitwise negation. It flips all the bits of its operand, changing 1s to 0s and 0s to 1s.

'''

print("\n=============Identity Operators=============")
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
