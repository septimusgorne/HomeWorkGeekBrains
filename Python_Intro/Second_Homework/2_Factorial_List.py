#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

numb = int(input())#Введите число
arr = []
temp = 1
for i in range(1, numb + 1):
    temp = temp * i
    arr.append(temp)
for j in arr:
    print(j, end=' ')
