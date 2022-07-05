# # A
# x = 4
# y = 7
# if x > y:
#     print("BIG")
# elif x < y:
#     print("small")
#
# # B
# for x in range(5):
#     print(x)
#
# # C
# season = 4
# if season == 1:
#     print("summer")
# elif season == 2:
#     print("winter")
# elif season == 3:
#     print("fall")
# elif season == 4:
#     print("spring")
#
# # D
# # 1. 10 times
# # 2. 10
#
# # E
# age = 28
# letter = 'T'
# dollar = 3.34
# flew = True
# apartment = 5
# print(age, letter, dollar, flew, apartment)
# print(age + dollar)
#
# # F
# phone_number = input("please enter your phone number: ")
# print("phone number:", phone_number)
#
# # G
# def printhello():
#     print("hello")
#
#
# def calculate():
#     print(5+3.2)
#
#
# printhello()
# calculate()
#
# # H
# def print_name(name):
#     print(name)
#
#
# def number_divide(number):
#     print(number/2)
#
#
# print_name("hadas")
# number_divide(9)
#
# # I
# def add_numbers(num1, num2):
#     return num1+num2
#
#
# add_numbers(3, 5)
#
#
# def strings(str1, str2):
#     return str1, str2
#
#
# strings('aaa', 'bbb')
#
# # J
# import array as arr
# a = arr.array('i', [3, 4, 5])
# for temp in a:
#     print(temp)
#
# # K
# numbers = [1, 3, 4, 7, 8]
# sum1 = 0
# for i in numbers:
#     sum1 += i
# print(sum1)
#
# # L
# dictionary = {'a': 1, 'b': 2, 'c': 3}
# for key in dictionary:
#     print(key)
#
# # Challenges:
# # M - pyramid shape
# for row in range(5):
#     for col in range(5):
#         if col <= row:
#             print("#", end="")
#     print()
#
# # N - X shape
# for row in range(7):
#     for col in range(7):
#         if (col == row) or (col + row == 6):
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
#
# # O
#
# def get_num():
#     num = int(input("please enter a number: "))
#     return num
#
#
# def sum_digit(a1):
#     result = 0
#     while a1 >= 1:
#         sum2 = int(a1 % 10)
#         a1 = int(a1 / 10)
#         result = result + sum2
#     return result
#
#
# a = get_num()
# print(a)
#
#
# b = sum_digit(a)
# print(b)
#
# # P
# x = 4, 2, 3, 4
# x = str(x)
# print(type(x))
# # another option:
# x = '4', '2', '3', '4'
# print(''.join(x))
#
# # Q
# my_list = [5, 6, 4, 7, 0, -2, 99]
# minimum = my_list[0]
# for i in range(len(my_list)):
#     if my_list[i] < minimum:
#         minimum = my_list[i]
# print(minimum)
