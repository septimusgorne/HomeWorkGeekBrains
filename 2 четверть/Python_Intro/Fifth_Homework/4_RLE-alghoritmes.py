#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(string):# Кодируем
    encoding = ''
    symb_last = ''
    n = 1
    while string != 0:
        for i in string:
            if i != symb_last:
                if symb_last:
                    encoding += str(n) + symb_last #Через привидение типа складываем строку
                n = 1
                symb_last = i
            else:
                n += 1
        else:
            encoding += str(n) + symb_last
        return encoding

def rle_decode(string):# Раскодируем
    decode = ''
    n = ''
    for i in string:
        if i.isdigit():#Проверяем на число
            n += i
        else:
            decode += i * int(n)
            n = ''
    return decode

def openFile(file):
    file = open("file_3.txt", 'r')#Открытие и чтение записанного файла
    for line in file:
        return line
    file.close

def write_file(name,str):
    with open(name, 'w') as data:
        data.write(str)
    data.close

def main():
############## Запускаем
    #show_1 = rle_encode('AAASAAADDSS')
    show_1 = rle_encode(input("Введите строку для кодирования: "))
    
    #print(show)# Для проверки
    write_file('file_3.txt', show_1)# Кодируем в файл
    
    printStr = openFile('file_3.txt')
    show_2 = rle_decode(printStr)
    write_file('file_4.txt', show_2)# Декодируем из файла
main()
