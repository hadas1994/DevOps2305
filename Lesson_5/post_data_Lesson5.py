import requests
res = requests.post('http://127.0.0.1:5000/user/4', json={"user_name": "ddd"})
if res.ok:
    print(res.json())
