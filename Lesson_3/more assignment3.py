# Task number 1
# Yes, because there is no index at position 5. Exists up to position 3.
# IndexError: list index out of range

# Task number 2
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    print(colors[i])

# Task number 3
# UnsupportedOperation or FileNotFoundError

# Task number 4
# Adds the mode: r+ , therefore if the file does not exist - the program will create it

# Task number 5-A
# Python program to explain os.mkdir() method
import os  # importing os module
directory = "test"  # Directory
parent_dir = "C:/Users/zhada/Desktop"  # Parent Directory path
path = os.path.join(parent_dir, directory)  # Path
os.mkdir(path)  # Create the directory
print("Directory '% s' created" % directory)

# Task number 5-B
my_name = open("C:/Users/zhada/Desktop/test/name.txt", 'w+', encoding='utf-8')
my_name.write("הדס")
my_name.seek(0)  # Returns the cursor to the 0 index
content = my_name.read()
print(content)
my_name.close()

# Task number 6 + Extra
# Creates a document in the following path: C:\Users\zhada\PycharmProjects\DevOps2305
from docx import Document
document = Document()
document.add_paragraph("hadas")
document.save('test.docx')
