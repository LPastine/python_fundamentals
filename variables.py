# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscorey
  - Can have numbers but can not start with one
"""
# x = 1
# y = 2.5
# name = 'Brad'
# isCool = True

# Multiple assignments
x, y, name, isCool = (1, 2.5, 'Brad', True)

print(x, y, name, isCool)

# Basic Math
a = x + y

print(a)

# Check Type
print(type(x))

# Casting
x = str(x)
y = int(y)

print(type(x))
print(type(y))
