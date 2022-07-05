# import pymysql
# from flask import Flask, request
#
# app = Flask(__name__)
#
# # local users storage
# users = {}
# # supported methods
# @app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
# def user(user_id):
#     if request.method == 'GET':
#         conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
#                                db='nUaXW57hSo')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM nUaXW57hSo.users;")
#         for row in cursor:
#             print(row)
#         cursor.close()
#         conn.close()
#         return {'user_id': user_id, 'user_name': users[user_id]}, 200  # status code
#
#     elif request.method == 'POST':
#         # getting the json data payload from request
#         request_data = request.json
#         # treating request_data as a dictionary to get a specific value from key
#         user_name = request_data.get('user_name')
#         users[user_id] = user_name
#
#         # Establishing a connection to DB
#         conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
#                                db='nUaXW57hSo')
#         conn.autocommit(True)
#         cursor = conn.cursor()
#         cursor.execute("INSERT into nUaXW57hSo.users (id, name) VALUES ('user_name', 'users[user_id]')")
#         cursor.close()
#         conn.close()
#         return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code
#
#   # todo elif for put and delete
#
#
# app.run(host='127.0.0.1', debug=True, port=5000)
#
import pymysql
from flask import Flask, request
from db_connector import insert_user
app = Flask(__name__)
users = {}


@app.route('/user/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                               db='nUaXW57hSo')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nUaXW57hSo.users;")
        for row in cursor:
            user_id = row[0]
            if user_id == user_id:
                print(row)
        cursor.close()
        conn.close()
        return {'status': 'OK', 'user_id': user_id, 'user_name': users[user_id]}, 200  # status code

    elif request.method == 'POST':
        import datetime
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name

        # insert_user(user_id, user_name)

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                               db='nUaXW57hSo')
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute("INSERT into nUaXW57hSo.users (user_id, user_name, creation_date) VALUES (%s, %s, %s)" %
                       (user_id, "'"+users[user_id]+"'", "'"+formatted_date+"'"))
        cursor.close()
        conn.close()
        try:
            return {'user id': user_id, 'user_added': user_name, 'creation date': formatted_date, 'status': 'ok'}, 200
            # status code
        except:
            return {"status": "error", "reason": "id already exists"}, 500  # status code

    elif request.method == 'DELETE':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            users[user_id] = user_name
            conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                                   db='nUaXW57hSo')
            conn.autocommit(True)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM nUaXW57hSo.users WHERE user_name = %s" % "'"+users[user_id]+"'")
            cursor.close()
            conn.close()
            return {'user_deleted': user_id, 'user name': user_name, 'status': 'ok'}, 200  # status code
        except:
            return {"status": "error", "reason": "no such id"}, 500  # status code

    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        users[user_id] = user_name
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                               db='nUaXW57hSo')
        conn.autocommit(True)
        cursor = conn.cursor()
        cursor.execute("UPDATE nUaXW57hSo.users SET user_id = %s WHERE user_name = %s"
                       % (user_id, "'"+users[user_id]+"'"))
        cursor.close()
        conn.close()
        return {'user id': user_id, 'user_updated': user_name, 'status': 'ok'}, 200  # status code


# todo elif for put and delete

@app.route('/get_all_users')
def get_all_users():
    if request.method == 'GET':
        all_users = []
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='nUaXW57hSo', passwd='3QG85WHfcS',
                               db='nUaXW57hSo')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM nUaXW57hSo.users;")
        for row in cursor:
            all_users.append(row)
        all_users = str(all_users)
        cursor.close()
        conn.close()

        return all_users, 200  # status code


app.run(host='127.0.0.1', debug=True, port=5000)
