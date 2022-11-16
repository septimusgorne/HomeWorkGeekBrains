# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random


def write_file(poe):
    with open('file.txt', 'w') as data:
        data.write(poe)

def randomNumb():
    return random.randint(0,100)

def create_degree(k):
    arr = [randomNumb() for i in range(k+1)]
    return arr

def create_str(point):
    arr= point[::-1]
    write = ''
    if len(arr) < 1:
        write = 'x = 0'
    else:
        for i in range(len(arr)):
            if i != len(arr) - 1 and arr[i] != 0 and i != len(arr) - 2:
                write += f'{arr[i]}x^{len(arr)-1-i}'
                if arr[i+1] != 0:
                    write += ' + '
            elif i == len(arr) - 2 and arr[i] != 0:
                write += f'{arr[i]}x'
                if arr[i+1] != 0:
                    write += ' + '
            elif i == len(arr) - 1 and arr[i] != 0:
                write += f'{arr[i]} = 0'
            elif i == len(arr) - 1 and arr[i] == 0:
                write += ' = 0'
    return write

k = int(input("Задайте натуральную степень k = "))
deg = create_degree(k)
write_file(create_str(deg))