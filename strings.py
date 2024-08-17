# name = 'Jawad'

# age = 22

# print('Hello, My name is ' + name + ' and I am '+ str(age))

# # String Formatting

# # Arguments by position

# print('My name is {name} and I am {age}'.format(name = name, age=age))

# # F-Strings (In python 3.6+)

# print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'computer science'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swapcase
print(s.swapcase())

# Length of the string
print(len(s))

# Replace
print(s.replace('science', 'engineering'))

# Count 
sub = 'c'
print(s.count(sub))
# Starts with
print(s.startswith('computer'))

# Ends with
print(s.endswith('e'))

# is all alphanumeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric

print(s.isnumeric())

