import requests

API_KEY = "your-app-api-key"
BASE_URL = "https://api.wattpad.com/v4/{}"

header = {
"Authorization": "Basic {}".format(API_KEY),
"Content-Type": "application/json",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
}

req = requests.get(BASE_URL.format("stories"), headers=header)
print(req.json())