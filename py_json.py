# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
USER_JSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to Dictionary
user = json.loads(USER_JSON)

print(user)
print(user['first_name'])

CAR = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(CAR)

print(carJSON)
