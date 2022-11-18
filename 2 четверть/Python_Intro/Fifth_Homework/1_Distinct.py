#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# 1. Входные и выходные данные хранятся в отдельных текстовых файлах.


##################### Ввод данных 1



#str = f"{input().split()}"# input str
str = input()# запусти этот ввод
#str = "АБВпоискпостроке"# проверка 
delStr = "абв"
#print(type(str))#checkType

##################### Создание файла 2

def write_file(name,str):
    with open(name, 'w') as data:
        data.write(str)
    data.close

###################### Открытие и чтение файла 3 

def openFile(file):
    file = open("file_1.txt", 'r')#Открытие и чтение записанного файла
    for line in file:
        return line
    file.close

##################### Удаление строки, фильтрация<+ создание и запись в файл> 4

def deleteName(str, delStr):
    with open('file_2.txt', 'w') as data:
        data.write(str.replace(f'{delStr}', ''))
        data.close
    return(str.replace(f'{delStr}', ''))

###################### Запуск 5

def main():
    #current = deleteName(str, delStr)
    # print(current)# проверка фильтра
    #str = "АБВпоискпостроке"
    write_file("file_1.txt", str)
    
    printStr = openFile('file_1.txt')#Открытие и чтение записанного файла
    print(f'Введённая строка записанная в файл text_1.txt {printStr}')
    current = deleteName(openFile('file_1.txt'), delStr)
    print(f'Изменённая строка записаная в файл text_2.txt: {current}')# проверка фильтра

main()
