# A class is like a blueprint for creating objects. An object has properties and methods (functions) associate with it. ALmost everything in Python is an object

class User:
    # Constructor
    def __init__ (self, name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1


Jawad = User('Jawad Ahmad', 'jawadahmad@gmail', 22)

# print(type(Jawad))

print(Jawad.email)
Jawad.has_birthday()

print(Jawad.greeting())

# Extend Class

class Customer(User):
    def __init__ (self, name,email,age):
        self.name = name
        self.email = email
        self.age = age
    def set_balance(self,balance):
        self.balance = balance
    # def greeting(self):
    #     return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    
# Init customer object

Sara = Customer('Sara Khan', 'Sara@gmail.com', 19)

Sara.set_balance(500)

print(Sara.greeting())