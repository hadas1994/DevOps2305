# # name = "Hadas"
# # last_name = "Tzafar"
# # age = 28
# # new_age = 7
# # print(name, last_name)
# # print(name, age)
# # print(name + ' ' + str(age))
# # print(age*new_age)
# # print(age+new_age)
# # print(age-new_age)
# # print(age/new_age)
# # print("My apt number is: " + str(age))
# a = 6
# b = 4
# if a > b:
#     print("good")
#     if a > 5:
#         print("a big than 5")
# elif b > a:
#     print(":(")
# # elif (a > b) and (a < 7):
# #     print(22)
# # elif (a > b) or (a < 7):
# #     print(24)
# else:
#     print("same number")
age = int((input("please enter your age:")))
if age > 18:
    print("Adult")
password = 12345
num = int((input("please enter your password:")))
if password == num:
    print("Logged in")
else:
    print("Access denied")
age = int((input("please enter your age:")))
height = int((input("please enter your height:")))
if age > 12 and height > 160:
    print("OK")
else:
    print("Forbidden")
