#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#array = [1.1, 1.2, 3.1, 5, 10.01]


########################Более длинный вариант, вспомнить сортировку

def quickSort (array):#Сортируем рекурсивно
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        grearrayter = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(grearrayter)

def sum (array):# Считаем сумму
    array = quickSort(array)
    return array[-1] - array[0]

def main():# Вводим и выводим :=)
    array = [float(i) for i in input().split()]
    #array = [1.1, 1.2, 3.1, 5, 10.01]# для проверки
    for i in range(len(array)):
        array[i] = array[i] % 1
    lists = quickSort(array)
    printes = sum(lists)
    print(f'Разница между максимальным и минимальным элементами массива: {float("{0:.3f}".format(printes))}'.format('.3f'))
    print(f'Разница между максимальным и минимальным элементами массива: {printes}')

main()# Поехали


###################Вариант короткий

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))