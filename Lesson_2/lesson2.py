# for x in range(5):
#     print(x, end="")
# print()
# for x in range(3, 5):
#     print(x, end="")
# print()
# for x in range(3, 8, 2):
#     print(x, end="")
# print()
#
# count = 0
# while count < 5:
#     print(count, end="")
#     count += 1
# print()
#
# count = 0
# while 1 > 0:
#     print(count)
#     count += 1
#     if count >= 5:
#         break
#
# def do_something():
#     print(1)
#     for x in range(10):
#         if x == 7 or x == 8:
#             continue
#         print(x, end="")
#
#
# do_something()
# print()
#
#
# def plus():
#     x = 2
#     y = 4
#     print(x + y)
#
#
# plus()
#
#
# def get_num():
#     return 2
#
#
# a = get_num()
# print(a)
#
#
# def my_name(name1):
#     print("my name is:", name1)
#
#
# name = input("please enter your name:")
# my_name(name)
#
import datetime
#
#
# def aaa(num10, num11):
#     print(num10 + num11)
#
#
# aaa(20, 55)
#
#
# # Grade 1 Exercise
# def num2():
#     return 5
#
#
# print(num2())
#
#
# # Grade 2 Exercise
# def num3(number):
#     print(number)
#
#
# num3(3)
#
# a = 1
#
#
# def abc():
#     x = 3
#     print(x)
#     print(a)
#
#
# def def2():
#     y = 900
#     print(y)
#
#
# abc()
# def2()
#

print(datetime.datetime.now())


my_list = [5, "a", True]
print(my_list)
my_list[0] = 6
print(my_list[0])
my_list.append(1234)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.insert(1, 7)
print(my_list)

new_list = [1, "x", False]
print(new_list[0])
new_list[0] = 10
print(new_list)
new_list.pop(2)
print(new_list)
print(len(new_list))

for temp in new_list:
    print(temp, end=" ")
print()

for i in range(len(new_list)):
    print(new_list[i], end=" ")
print()

x_tuple = 1, 2, 3, 4, 5
y_tuple = ('a', 'b', 'c', 'd')
tup = 1, "a", 4


my_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(my_dictionary['a'])
print(my_dictionary.keys())
print(my_dictionary.values())
del(my_dictionary['a'])
print(my_dictionary)
