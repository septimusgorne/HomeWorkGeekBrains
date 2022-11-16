#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#######################################

from math import ceil
a = [int(i) for i in input().split()] 
b = []
for i in range(ceil(len(a)/2)):
        b.append(a[i] * a[-1 - i])
print(b)

#######################################


# arr = [2, 3, 4, 5, 6, 7]
# b = []

# def mult(arr):
#     mult = 0
#     multLast = 1
#     for index, value in enumerate(arr / 2):
#         # #b.append(arr[index] * arr[index - 1])
#         # mult = (arr[index] * arr[index - 1])
#         # arr.pop(index) and arr.pop(index - 1)            
#         # b.append(mult)
#         # mult(arr[index])
#         # print("Остаток",arr)

#         print(arr)

# mult(arr)


# a = [2, 3, 4, 5, 6] 
# b = []
# for i in range((len(a)/2)):
#     # if len(a) >= 3:
#         # mult = (a[i] * a[-1 - i])
#         # b.append(mult)
#         a.pop(a[i], a[-1 - i])
#         print(a)
#     # elif len(a) == 3:
#     #     b.append(a[i + 1] * a[i + 1])
# print(b)

# a = [2, 3, 4, 5, 6] 
# b = []

# mult = 1
# for i in range(ceil(len(a)/2) - 1):
#     print(a)
#     minIndex = a[0 + i]
#     maxIndex = a[-i-1]
#     #b.append(minIndex * maxIndex)
#     a.pop(minIndex) and a.pop(maxIndex)
#     print(a)
# print("Массив Б", b)
