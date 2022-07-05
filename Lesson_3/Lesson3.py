# my_file = open("C:/Users/zhada/Desktop/1.txt", 'a+', encoding='utf-8')
# my_file.seek(0)  # Returns the cursor to the 0 index
# content = my_file.read()
# print(content)
#
# content2 = my_file.write("tzafar")
# print(content2)  # Prints the number of letters in the word
#
# my_file.seek(0)
# content = my_file.read()
# print(content)
#
# my_file.close()  # resource release

try:
    my_file = open("C:/Users/zhada/Desktop/2.txt", 'r')
    x = my_file.write('aaaa')
    print(x)
    my_file.close()
    x = 1/0
except IOError as e:
    print(e)  # The value of an object e
finally:
    print("hello")

print("123")
