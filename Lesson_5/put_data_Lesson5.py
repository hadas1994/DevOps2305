import requests
res = requests.put('http://127.0.0.1:5000/user/2', json={"user_name": "John"})
if res.ok:
    print(res.json())
