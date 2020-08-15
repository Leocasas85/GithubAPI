import requests
import json

url = "https://api.github.com/users/<Username>"

payload = ""
headers = {
    'Authorization': "Bearer <Your Token",
    'cache-control': "no-cache",
    'Postman-Token': "<Take from postman raw view>"
    }

response = requests.request("GET", url, data=payload, headers=headers)

pretty_data = json.dumps(response.json(), indent=5)

print(pretty_data)
