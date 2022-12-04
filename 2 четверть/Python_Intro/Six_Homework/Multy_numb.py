#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#######################################

# from math import ceil
# a = [int(i) for i in input().split()] 
# b = []
# for i in range(ceil(len(a)/2)):
#         b.append(a[i] * a[-1 - i])
# print(b)


lists = [input().split(',')]
data = list(enumerate(lists))
print(data)