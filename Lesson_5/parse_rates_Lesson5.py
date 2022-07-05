import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers = {
  "apikey": "2t3yGvZ1j2x3PT2Rz3GO0N9vjre2LIKv"
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
print(data)
results = data['result']
print(results)
