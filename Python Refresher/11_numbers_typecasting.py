'''
There are three numeric types in Python:
    - int
        - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    - float
        - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
        - Float can also be scientific numbers with an "e" to indicate the power of 10.
            - z = -87.7e100
            - y = 12E4
    - complex
        - Complex numbers are written with a "j" as the imaginary part:
            - x = 3+5j
            - y = 5j
            - z = -5j

Type Conversion:
    - can convert fro one type to another with the int(), float(), and complex() methods by typecasting
    - Note: you can not convert complex numbers into another number type

Random Number:
    - Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
'''

# Numeric Types and Conversions
print("---------Numeric Types and Conversions----------")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)        # 1.0
print(b)        # 2
print(c)        # (1+0j)

print(type(a))
print(type(b))
print(type(c))

print("/n/n")


######################################################
print("-----------Random Number----------")
# Import the random module, and display a random number from 1 to 9:
import random

print(random.randrange(1, 10))

'''
print(random.randint(1, 10))   # 1 to 10 inclusive
print(random.randrange(1, 10)) # 1 to 9
print(random.random())         # 0.0 <= x < 1.0
print(random.uniform(1, 10))   # 1.0 <= x <= 10.0 (practically)
'''