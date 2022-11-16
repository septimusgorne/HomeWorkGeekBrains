# Задача 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

############################################################## запись в файл
def write_file(name,poe):
    with open(name, 'w') as data:
        data.write(poe)

############################################################# создание случайного числа от 0 до 100
def randomNumb():
    return random.randint(0,100)

############################################################# создание коэффициентов многочлена
def create_degree(k):
    arr = [randomNumb() for i in range(k+1)]
    return arr
    
############################################################# создание многочлена в виде строки 
def create_str(point):
    arr= point[::-1]
    wr = ''
    if len(arr) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(arr)):
            if i != len(arr) - 1 and arr[i] != 0 and i != len(arr) - 2:
                wr += f'{arr[i]}x^{len(arr)-i-1}'
                if arr[i+1] != 0 or arr[i+2] != 0:
                    wr += ' + '
            elif i == len(arr) - 2 and arr[i] != 0:
                wr += f'{arr[i]}x'
                if arr[i+1] != 0 or arr[i+2] != 0:
                    wr += ' + '
            elif i == len(arr) - 1 and arr[i] != 0:
                wr += f'{arr[i]} = 0'
            elif i == len(arr) - 1 and arr[i] == 0:
                wr += ' = 0'
    return wr
############################################################ получение степени многочлена
def sq_degree(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

########################################################### получение коэффицента члена многочлена
def k_degree(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num
############################################################ разбор многочлена и получение его коэффициентов
def calc_degree(poe):
    poe = poe[0].replace(' ', '').split('=')
    poe = poe[0].split('+')
    arr = []
    l = len(poe)
    k = 0
    if sq_degree(poe[-1]) == -1:
        arr.append(int(poe[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if sq_degree(poe[ii]) != -1 and sq_degree(poe[ii]) == i:
            arr.append(k_degree(poe[ii]))
            ii -= 1
            i += 1
        else:
            arr.append(0)
            i += 1
        
    return arr
    
########################################################## создание двух файлов

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
deg1 = create_degree(k1)
deg2 = create_degree(k2)
write_file("file_1.txt", create_str(deg1))
write_file("file_2.txt", create_str(deg2))

########################################################## нахождение суммы многочлена
with open('file_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
arr2 = calc_degree(st1)
arr3 = calc_degree(st2)
ll = len(arr2)
if len(arr2) > len(arr3):
    ll = len(arr3)
arr_new = [arr2[i] + arr3[i] for i in range(ll)]
if len(arr2) > len(arr3):
    dee = len(arr2)
    for i in range(ll,dee):
        arr_new.append(arr2[i])
else:
    dee = len(arr3)
    for i in range(ll,dee):
        arr_new.append(arr3[i])
write_file("file34_res.txt", create_str(arr_new))
with open('file34_res.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")