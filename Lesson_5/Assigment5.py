# Database
import pymysql
conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS', db='nUaXW57hSo')
conn.autocommit(True)
cursor = conn.cursor()
# 2
cursor.execute("INSERT into nUaXW57hSo.dogs (name, age, breed) VALUES ('Marley', 3, 'Labrador')")
cursor.execute("INSERT into nUaXW57hSo.dogs (name, age, breed) VALUES ('Sushi', 5, 'Maltese')")
cursor.execute("INSERT into nUaXW57hSo.dogs (name, age, breed) VALUES ('Bamba', 6, 'Pekingese')")
# 3
cursor.execute("UPDATE nUaXW57hSo.dogs SET age = 4 WHERE name = 'Sushi'")
# 4
cursor.execute("DELETE FROM nUaXW57hSo.dogs WHERE name = 'Bamba'")
# 5
cursor.execute("SELECT * FROM nUaXW57hSo.dogs;")
for row in cursor:
    print(row[0])
cursor.close()
conn.close()

# REST API - 1
import requests
url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"
payload = {}
headers = {"apikey": "2t3yGvZ1j2x3PT2Rz3GO0N9vjre2LIKv"}
response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()
results = data['result']
print("The dollar exchange rate is:", results)
amount = float(input("Please enter an amount of Shekels to convert to Dollars: "))
print("The result:", results * amount)

# REST API -2
import pymysql
from flask import Flask, request

app = Flask(__name__)


@app.route('/dogs')
def user():
    if request.method == 'GET':
        dogs = []
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                               db='nUaXW57hSo')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nUaXW57hSo.dogs;")
        for row in cursor:
            dogs.append(row)
        dogs = str(dogs)
        cursor.close()
        conn.close()

        return dogs, 200 # status code


app.run(host='127.0.0.1', debug=True, port=50000)
