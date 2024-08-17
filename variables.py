"""
-Variable names are case sensitive (name and NAME are different variables)
-Must start with a letter or an underscore
- Can have numbers but can not start with one
"""
a = 1 # Integer Data type

b = 5.9 # float

c = 'Jawad Ahmad' #String

check = True # Boolean

# We can assign values in one line also

a,b,c,check = (1,5.9, 'Jawad Ahmad',True)
# Casting 

a = str(a)

b = int(b)

b = float(a)

print(type(b))
