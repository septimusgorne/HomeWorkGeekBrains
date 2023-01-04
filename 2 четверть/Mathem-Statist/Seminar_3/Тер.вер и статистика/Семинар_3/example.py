
#4 карты из 36 сколько вариантов
import numpy as np
from math import factorial

def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

comb = (f'{combinations(11, 2)} Вариантов сочетаний')

print(comb)

#Сколькими способами могут 5 человек из 20

# def arrangements(n, k):
#     return np.math.factorial(n) // np.math.factorial(n - k)

# res = arrangements(144, 70)

# print(res)

#Сколькими способами 5 покупателей могут образовать очередь

# def arrangements(n):
#     return np.math.factorial(n)

# res = arrangements(8)

# print(res)

# def combinations(l,m):
#     return ((l**m)/np.math.factorial(m)) * np.math.exp(-l)

# comb = (f'{combinations(2, 0)}')

# print(comb)