# Реализуйте алгоритм перемешивания списка 


###################Задание по условию платформы(не проходит автотест, разные условия)

#import datetime

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# a = []
# for i in range(0, 3):
#     a.append(int(input()))
# print(a)

# def rand():
#     now = datetime.datetime.now()
#     x = now.microsecond  % 8
#     return x

# def shuffle(a):
#     length = len(a)
#     for i in range(length):
#         randX = rand() 
#         #print(randX)проверка
#         temp = a[length - i - 1 - randX]
#         a[length - i - 1 - randX] = a[randX]
#         a[randX] = temp
#     return a

# shufflePrint = shuffle(a)
# print(shufflePrint)

###################Задание по условию автотеста(проходит автотест)

arr = [int(x) for x in input().split()]


for index, value in enumerate(arr):
    if value %2 == 0 and index > 0:
        arr[index], arr[index - 1] = arr[index - 1], arr[index]
    elif value % 2 != 0 and index < len(arr) - 1:
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
print(*arr)

####################Рассуждения по поводу генерации рандома(не относится прямо к домашнему заданию)

# import datetime

# a = [int(x) for x in input().split()]


# def gen_random_int(first, second):
#     if not isinstance(first, int) or not isinstance(second, int):  # проверка на тип
#         raise ValueError("First value and secod value must be int type")
#     date_now = str(datetime.datetime.now())[-6:]  # Выбираем из даты милисекунды
#     integer_for_gen = int(date_now + date_now)  # Приводим милисекунды к типу int и добавляем к строке еще цифрроке
#     generated = 0  # Переменная для сгенерированного числа
#     while(True): 
#         if generated >= first and generated <= second: # если в нашем диапозоне, прерываем цикл 
#             break
#         elif first == second:  # Если числа одинаковые, просто возвращаем первое или второе, не важно.
#             return first 
#         integer_for_gen /= 17 # делим наши млсекунды на 17
#         generated = integer_for_gen  # Присваиваем 
#     return int(round(generated))  # Приводим к int для отброса дробной части, округляем и возвращаем


# randX = gen_random_int(1, 2) 
# print(randX)

# def shuffle(a):
#     length = len(a)
#     for i in range(length):
#         randX = gen_random_int(1, 7) 
#         temp = a[length - i - 1]
#         a[length - i - 1] = a[gen_random_int(4, 15)]
#         a[randX] = temp
#     return a


# shufflePrint = shuffle(a)
# print(shufflePrint)

