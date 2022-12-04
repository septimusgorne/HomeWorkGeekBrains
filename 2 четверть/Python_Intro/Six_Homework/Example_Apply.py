# Файл с черновиками использования функций
# 
# def f(x):
#     x**2
#     return x

# g = f
# print(type(f(2)))
# print(type(g))

#############################
# def mult(x, y):
#     return x * y
# def delt(x, y):
#     return x - y


# # def sum(x, y):
# #     return x + y
# # #f = sum
# sum = lambda x, y: x + y#;lambda

# def calculation(fun, numb1, numb2):
#     print(fun(numb1, numb2))
#     return fun(numb1, numb2)

# def main():
#     # calculation(f, int(input), int(input))
#     #calculation(sum, 4, 10)
#     calculation(lambda x, y: x + y, 4, 5)#lambda

# main()

################################

#List Comprehension Быстрое создание списков

# [exp for item in iterable] #есть некое выражение. после пишем item in (некий итерируемый объект)
# [exp for item in iterable (if conditional)] #по условию
# [exp <if condi>tional> for item in iterable (if conditional)]


# list = []
# for i in range(1, 101):
#     if(i%2 == 0):
#         list.append(i)
# print(list)


# list = []
# for i in range(1, 101):
#     #if(i%2 == 0):
#         list.append(i)
# print(list)

# list =[i for i in range(0, 15)] # создание списка
# list2 = [i for i in range(1, 21) if i%2 == 0] # создание списка с условием
# list3 = [(i, i + 1) for i in range(0, 20) if i % 2 == 0] # с кортежами(пары чисел)

# def f(x):
#     return x ** 3
# list4 = [f(i) for i in range(0, 21) if i % 2 == 0]# подключили функцию
# list5 = [(i, f(i)) for i in range(0, 10) if i % 2 == 0]# подключили кортежи(число, куб числа)

# print(list5)

#Анонимные лямбда-функции

# В файле хранятся числа, нужно выбрать четные и составить список пар(число, квадрат числа)

# Пример: 1 2 3 4 5 6 7 8 9 => 2 4 6 8 => [(2, 4), (4, 16), (6, 36), (8, 64)]

# def write_file(name_file, str):
#     with open(name_file, "w") as numbers_list:
#         numbers_list.write(str + ' ')
#     numbers_list.close

# def open_file(name_file):
#     name_file = open("file_lection_work1.txt", "r")
#     for line in name_file:
#         while line != ' ':
#             return line
#     name_file.close

# def calculation(string):
#     list = [(i, i**2) for i in range(0, len(string)) if i %2 == 0]
#     return list

# def main():
#     # write_file("file_lection_work1.txt", input())
#     write_file("file_lection_work1.txt", "2, 7, 3, 14, 15, 63, 7, 81, 91, 10")
#     show = open_file("file_lection_work1.txt")
#     printes = calculation(show)
#     print(printes)
# main()

############################
# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return [x for x in col if (f(x))]

# data = '1 2 3 4 5 8 19 23 1 43 1 54'.split()

# #list = select(int, data)
# #print(list)
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x, x**2), res)
# print(res)
#############################

#Map

# li = [x for x in range(1 ,20) if x%2 == True]

# li = list(map(lambda x: x + 10, li))#каждое число увеличивается на 10

# print(li)


##########################
# data = list(map(int, input().split()))#список пробрасываем функцию map

# print(data)

# for e in data:
#     print(e)


# def where(f, col):
#     return [x for x in col if (f(x))]

# data = '1 2 3 4 5 8 19 23 1 43 1 54'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x:(x, x**2), res))
# print(res)

########Fliter

# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)

###################

# data = '1 2 3 4 5 8 19 23 1 43 1 54'.split()

# res = map(int, data)
# res = list(filter(lambda x: not x%2, res))
# res = list(map(lambda x:(x, x**2), res))
# print(res)


########ZIP

# zip([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])


user = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,3333]

# data = list(zip(user, ids, salary))
# print(data)

#####Enumerate

data = list(enumerate(user))
print(data)
