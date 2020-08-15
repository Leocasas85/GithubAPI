import requests
import json

url = "https://api.github.com/users/hpidcock"

payload = ""
headers = {
    'Authorization': "Bearer 3cdbd1755b417f6e829a77fdee2d7fcc87b20436",
    'cache-control': "no-cache",
    'Postman-Token': "925dcaab-f487-4d56-9ec9-4e94f29e5007"
    }

response = requests.request("GET", url, data=payload, headers=headers)

pretty_data = json.dumps(response.json(), indent=5)

print(pretty_data)