import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS', db='nUaXW57hSo')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# # Inserting data into table
# cursor.execute("INSERT into nUaXW57hSo.users (name, id) VALUES ('john', 5)")

# Getting all data from table “users”
cursor.execute("SELECT * FROM nUaXW57hSo.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

# # Updating data inside the table
# cursor.execute("UPDATE nUaXW57hSo.users SET id = '10' WHERE name = 'john'")

# # Deleting data into table
# cursor.execute("DELETE FROM nUaXW57hSo.users WHERE name = 'john'")

cursor.close()
conn.close()
