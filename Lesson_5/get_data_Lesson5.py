import requests
res = requests.get('http://127.0.0.1:5000/user/1')
if res.ok:
    print(res.json())
# , json={"user_name": "Hadas"}