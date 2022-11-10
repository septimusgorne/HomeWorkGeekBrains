#print('hello чувак')


# #balis = NONE
# a = 123
# b = 1.23
# print(a)
# print(type(a))
# #balis = 'lols'
# s = 'howewer'

# #print (s) # вывод переменной S
# #print('-первая переменная-',a, '-вторая переменная-', b ,"-третья переменная-", s)
# print ('{} - {} - {}'.format(a, b, s)) 
# print (f'{a} - {b} - {s}')
# print('{2} - {0} - {1}'.format(a, b, s))

# f = True
# print(f)


# list = [1, 4, 6]
# print(list)

# list2 = ['s','z', 234, false, 1.23]
# print(list2)

#Ввод переменных
# print ('Введите переменную a')
# a = int(input())
# print('Введите переменную b')
# b = int(input())
# #print(f'Значение переменной a = {a}, Значение переменной b = {b}')
# print(a, '+', b, '=', a + b)

# a = 12
# b = 1.3
# c = a % b
# print(c)

# a = 2
# b = 4
# c = a ** b
# print(c)

# a = 1.32343
# b = 3
# c = round(a * b, 3) 
# print(c)

# a = 3
# a += 5
# print(a)


# a = 1 > 4 and 5 > 3
# b = 1 != 2
# print(a, b)

# a = [1, 2, 3]
# b = ['1', '2', '3']# false
# c = [1, 2, 3]
# print(a == b or a == c)

# a = 1 < 2 < 6 < 10
# print(a) 

# func = 1
# T = 4
# x = 123
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f)
# print(not 6 in f)


# s = [1, 2, 3, 4]
# is_Odd = s[0] % 2 == 0
# print(is_Odd)

# x = [1, 2, 3, 4]
# is_Odd =not x[0] % 2 == 0
# print(is_Odd)


#if-else

# print("Введите число а")
# a = int(input())
# print("Введите число b")
# b = int(input())
# print("Наибольшее число")
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя')
# if username == 'Артур':
#     print("Здарова братан")
# elif username == 'Инна':
#     print("Привет Иннуся")
# else:
#     print('Привет', username)

# origin = 23
# inverted = 0
# while origin != 0:
#     inverted =inverted * 10 + (origin % 10)
#     origin //=10
# print(inverted)

# origin = 23
# inverted = 0
# while origin != 0:
#     inverted = inverted * 10 + (origin % 10)
#     origin //= 10
#     print(origin)
# else:
#     print('Пожалуй')
#     print('хватит')
# print(inverted)

# for i in 1,2,3,4,5,6:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i)

# r = range(10)#object range
# for i in r:
#     print(i)


# for i in r(5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in "wertet":
#     print(i)

#String

# text = "Каждый охотник желает знать, где живёт фазан"

# print(len(text))# how much symbols/COUNT
# print('еще' in text)# Search in string true/false
# print(text.isdigit())
# print(text.islower())
# print(text.replace('охотник', 'ЕЩЕ'))

# for s in text:
#     print(s)

# text = "Каждый охотник желает знать, где живёт фазан"
# #print(text.capitalize)

# help(text.capitalize)

# text = "Каждый охотник желает знать, где живёт фазан"
# print(text[0]) # К
# #print(text[len(text)]) #Error because index array 0 in lists
# print(text[-5]) #ф because index lastArray -1 => equals "ф"
# print(text[:]) # for 0 than len(text - 1)
# print(text[:5]) # for 0 than 5 symols
# print(text[len(text) - 2:]) # this array for -2 array(Last) than LAST
# print(text[2:4]) # arra 2 than 4 element array
# print(text[0:len(text):5]) #

#LISTS

# numbers = [1,2,3,4,5,6]
# #print(type(numbers))
# ran = range (1, 4)
# numbers = list(ran)
# print(type(numbers))
# print(f'{len(numbers)} len')
# #print(type(ran))

# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e) # red green blue

# for e in colors:
#     print(e*2) # redred greengreen blueblue

# colors.append('gray') # add in lasr List
# print(colors == ['red', 'green', 'blue', 'gray']) # true
# colors.remove('red') # delete colors[0]


#Function

def f(x):
    if x == 1:
        return 'This is one'
    elif x == 2.5:
        return 'sdfsdfsdf'
    else:
        return
arg = 2.5
print(f(arg))
print(type(f(arg)))
