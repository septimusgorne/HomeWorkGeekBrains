# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print("Введите число")
# numb = float(input()) or int(input())
# sum = 0
# while numb != 0:
#     temp = numb % 10
#     sum += temp
#     numb //= 10
# print(sum)

######################################################################
# num = input("Введите дробное, через ,: ")
# x = num.split(".")
# a = int(x[0]) # целая часть
# b = int(x[1]) # дробная часть   
# sum = 0
# res = 0
# while (a != 0):
#     sum = sum + (a % 10)
#     a = a // 10
# while (b != 0):
#     sum = sum + (b % 10)
#     b = b // 10
# print("Сумма цифр дробного числа:", sum)
# if b == 0:
#     while (a != 0): 
#         res = res + (a % 10)
#         a = a // 10
#         print(res)
#######################################################################
   


# num = input("Введите дробное, через ,: ")
# # разделим введённое (тип данных строка) на две части
# x = num.split(".")
# a = int(x[0]) # целая часть
# b = int(x[1])
# res = 0
# sum = 0

# if "." in x:
#     #b = int(x[1]) # дробная часть
#     sum = 0
# while (a != 0): 
#     sum = sum + (a % 10)
#     a = a // 10
# while (b != 0): 
#     sum = sum + (b % 10)
#     b = b // 10
#     print("Сумма цифр дробного числа:", sum)
# else:
#     while (a != 0): 
#         res = res + (a % 10)
#         a = a // 10
#     print("Сумма цифр целого числа", res)
   

numb = input().split()#Введите число
numb = ' '.join(numb)
sum = 0
for el in numb:
    if el.isdigit():
        sum+=int(el)
print(sum)