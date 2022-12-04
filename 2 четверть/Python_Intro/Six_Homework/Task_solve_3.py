#Нахождение квадрата чисел в введенных числах

data = '1 2 3 4 5 8 19 23 1 43 1 54'.split()

res = map(int, data)
res = list(map(lambda x:(x, x**2), res))
print(res)