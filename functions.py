# A function is a block of code which only runs when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces

# Create Function

def sayHello(name):
    print(f'Hello {name}')



# Return values
def getSum(num1,num2):
    total = num1+num2

    return total


# print(getSum(3,4))

# A lambda function is a small anonymous function
# Can take any number of arguments but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1,num2 : num1 + num2 

print(getSum(10,23))