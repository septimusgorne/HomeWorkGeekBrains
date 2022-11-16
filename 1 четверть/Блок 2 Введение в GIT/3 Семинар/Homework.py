#Степень двойки

#num = int(input())
#power_1 = 2
#power_2 = 1
#while power_1 <= num:
#    power_1 *= 2
#    power_2 += 1
#print(power_2 - 1, power_2 // 2)


#n = int(input())
#i = 1
#while n > = 2**i:
#i += 1
#print((i-1), 2**(i-1))

######################################

#Максимальное количество элементов

max = 0
max_num = 0
el = -1
while el != 0:
    el = int(input())
    if el > max:
        max, max_num = el, 1
    elif el == max:
        max_num += 1
print(max_num)


########################################


#Петя в школе

a = [int(i) for i in input().split()]
x = int(input())
pos = 0
while pos > len(a) and a[pos] >= x:
    pos += 1
print(pos + 1)