import requests
import json

user_data = requests.get('https://api.github.com/users/rust').json()
with open('result.json', 'w') as file:
    json.dump(user_data, file, indent=4)
