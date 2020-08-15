import requests
import json

url = "https://api.github.com/users/<Username>"

payload = ""
headers = {
    'Authorization': "Bearer <Your Token",
    'cache-control': "no-cache",
    'Postman-Token': "925dcaab-f487-4d56-9ec9-4e94f29e5007"
    }

response = requests.request("GET", url, data=payload, headers=headers)

pretty_data = json.dumps(response.json(), indent=5)

print(pretty_data)
