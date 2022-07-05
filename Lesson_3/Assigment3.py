# Task number 1
a = 1/0

# Task number 2
try:
    a = 1/0
except ZeroDivisionError as e:
    print(e)

# Task number 3
# The following code is invalid because the "finally" is indentation under "Try". It should be in line 0.
# SyntaxError: invalid syntax

# Task number 4
my_file = open("/Python_Error_Types_(Exceptions).txt")
content = my_file.read()
print(content)
my_file.close()

# Task number 5
# The use of bare except is not recommended because we do not know which exception we caught.
# In addition, it indicates a lack of knowledge in writing code.

# Task number 6
# examples for IOError: UnsupportedOperation, FileNotFoundError, No permissions and more ...
# example for ZeroDivisionError: division by zero

# # Task number 7 + 8 + 9
new_file = open("/words.txt", 'w+')
content1 = new_file.write("hadas")
new_file.seek(0)
content2 = new_file.read()
print(content2)
new_file.close()

# Task number 10
my_name = open("C:/Users/zhada/Desktop/3.txt", 'w+', encoding='utf-8')
my_name.write("הדס")
my_name.seek(0)  # Returns the cursor to the 0 index
content = my_name.read()
print(content)
my_name.close()

# Task number 11
from flask import Flask

app = Flask(__name__)

# returns the content of any txt file


@app.route("/content")
def content():
    my_file11 = open("C:/Users/zhada/Desktop/4.txt", 'r', encoding='utf-8')
    my_file11.seek(0)  # Returns the cursor to the 0 index
    content11 = my_file11.read()
    return content11, 200  # status code

# writes the word “hello” into any txt file and return “success”


@app.route("/register")
def register():
    my_file12 = open("C:/Users/zhada/Desktop/5.txt", 'w', encoding='utf-8')
    my_file12.write("hello")
    return "success", 201  # status code


app.run(host='localhost', debug=True, port=30000)

# Task number 12

from PIL import Image

width = 400
height = 300

img = Image.new(mode="RGB", size=(width, height), color=(209, 123, 193))
img.show()
