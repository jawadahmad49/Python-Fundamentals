# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules can be installed using pip package manager (Including Django) as well as custom modules

# import datetime
# from datetime import date
# from time import time
# # today = datetime.date.today()

# today = date.today()

# timestamp = time()

# print(timestamp)


# Pip Module
from camelcase import CamelCase

c = CamelCase()

print(c.hump('hello there world'))


# Import custom module

import validator
from validator import validate_email

email = "test@test.com"
if validate_email(email):
    print("Valid Email!")