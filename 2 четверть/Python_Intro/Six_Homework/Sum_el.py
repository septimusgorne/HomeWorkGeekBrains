#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum(arr):
#     sum = 0
#     for index, value in enumerate(arr):
#         if index % 2 != 0 and index < len(arr):
#             sum += value
#             print(f'на нечётных позициях элементы {index} и {index + 1}, ответ: {sum}')
#     print(f'Сумма нечётных элементов: {sum}')

# def main():
#     sum(arr = [int(x) for x in input().split()])


lst = []
lst = list(map(int, input('Enter digits - interval: ').split())) 

def summaOdd(lst): 
    countSum = 0 
    for i in range(len(lst)): 
        if i%2 != 0: 
            countSum+=lst[i] 
            print(countSum) 
    summaOdd(lst)

summaOdd(lst)
