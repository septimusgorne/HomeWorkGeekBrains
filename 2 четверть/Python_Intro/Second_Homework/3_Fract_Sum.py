#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#  (1+ 1/n)n

n=int(input())#Введите число
a = []
sum = 0
for i in range(1, n + 1):
    form = ((1+1/i)**i)
    sum += form
    a.append(form)#для проверки
print(round(sum, 2))