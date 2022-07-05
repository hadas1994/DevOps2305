import requests
res = requests.delete('http://127.0.0.1:5000/user/3', json={"user_name": "ccc"})
if res.ok:
    print(res.json())
