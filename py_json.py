# JSON is commonly used with data APIs. Here how we can pasrse JSON into a python dictionary

import json

userJSON = '{"first_name":"John", "last_name":"Doe","age":30}'

# Parse to dict
# user = json.loads(userJSON)

# print(user['first_name'])

car = {'make':'Ford', 'model':'Mustang', 'year':1970}

carJSON = json.dumps(car)

print(carJSON)