import requests
import json

API_KEY = "AVMHeV6pxPlMksujAClTZYB9ylNpKnKdJWLUOVDogtwz"
BASE_URL = "https://api.wattpad.com/v4/{}"

header = {
"Authorization": "Basic {}".format(API_KEY),
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

req = requests.get(BASE_URL.format("stories"), headers=header)
json_response = req.json()
print(json.dumps(json_response, indent=3, sort_keys=True))
