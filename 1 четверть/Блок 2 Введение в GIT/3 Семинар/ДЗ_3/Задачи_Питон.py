# Задача «Шеренга»

a=[int(i) for i in input().split()]
b = int(input())
N=0
while N<len(a) and a[N]>=b:
    N+=1
print(N+1)

#######################

#Задача «Количество элементов, равных максимуму»

ch=int(input())
m=ch
k=1
while ch!=0:
    ch=int(input())
    if ch==m:
        k+=1
    if ch>m:
        m=ch
        k=1
print(k)

#######################

#Задача «Степень двойки»

n = int(input())
a = 2
b = 1
while a <= n:
    a *= 2
    b += 1
else:
    print(b - 1, a // 2)
