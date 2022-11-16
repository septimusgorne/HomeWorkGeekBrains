#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

###################Реализация по условию на автотесте(не проходит автотест)

# x = int(input("Введите длину строки: "))

# spisok1 = []#количество элементов [0] и множители
# spisok2 = []#список чисел

# for j in range(x):
#     i = spisok1.append(int(input()))
# print(spisok1)#проверка

# for i in range(-spisok1[0], spisok1[0] + 1):
#         spisok2.append(i)
# print(spisok2)#проверка

# def inputMult():
#     prod = 1
#     spisok1[0] = spisok1[1]
#     for i in range(spisok1[0], len(spisok1)):
#         for j in spisok2:
#             if spisok1[i] == j:
#                 prod *= spisok2[i]
#         print(f' "Произведение индекса {spisok1[i]} на значение {spisok2[i]} равно {prod}')#проверка
#     print(f'Произведение равно {prod}')

# inputMult()

##########################Задание по условию платформы(проходит автотест)

N = int(input())
spisok1 = [i for i in range(-N, N+1)]

spisok2 = [i for i in input().split()]
with open('file.txt', 'w') as data:
    for i in range (len(spisok2)):
        data.writelines(str(spisok2[i])+'\n')
mult = 1
path = 'file.txt'
data = open(path, 'r')
for i in data:
    mult *= spisok1[int(i)]
data.close()
  
print(mult)