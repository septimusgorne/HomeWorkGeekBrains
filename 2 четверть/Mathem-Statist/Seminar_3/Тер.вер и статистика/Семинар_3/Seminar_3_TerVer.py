import numpy as np
import statistics
from math import factorial

#Среднеквадр.отклонение
def stdev(nums):
    diffs = 0
    avg = sum(nums)/len(nums)
    for n in nums:
        diffs += (n - avg)**(2)
    return (diffs/(len(nums)-1))**(0.5)

#Дисперсия
def variance(xs):
    mu = sum(xs) / len (xs)
    n = len(xs)
    n = n-1 if n in range(1, 30) else n  #30
    square_deviation = lambda x : (x - mu) ** 2 
    return sum( map(square_deviation, xs) ) / n

#Вывод результатов для первой задачи
def calculation_1():
    arr = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
    print (f"Среднее арифм. = {sum(arr) / len(arr)}")
    print(f"Среднее арифм. = {statistics.mean(arr)}")

    print (f"Среднеквадр. отклонение ={statistics.stdev(arr)}")
    print(f"Среднеквадр. отклонение ={stdev(arr)}") # вывожу специально двумя видами для проверки

    print(f"Несмещенная дисперсия = {variance(arr)}")
    print(f"Несмещенная дисперсия = {statistics.variance(arr, sum(arr)/len(arr))}")

    #print(f"Смещенная дисперсия = {variance(arr)}")
    print(f"Смещенная дисперсия! = {statistics.variance(arr, 20)}") # допустим, для 20 вместо методики расчета по среднему 65.3
    

calculation_1()


# def combinations(n,k):
#     return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

# comb = (f'{combinations(3, 0)} Вариантов сочетаний')

# print(comb)