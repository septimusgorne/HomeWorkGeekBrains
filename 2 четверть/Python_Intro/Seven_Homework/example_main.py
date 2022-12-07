
import string

#Вводим данные
def input_data():
    print("Введите данные в справочник")
    first_name = input('Имя:')
    last_name = input('Фамилия')
    number_phone = input('Номер телефона')
    comment = input('Комментарий')
    list_phonebook = [first_name, last_name, number_phone, comment]
    numb_phonebook = int(input('Введите номер в списке контактов: '))

    dict = (numb_phonebook, str(list_phonebook))
   
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(str(dict) + '\n')
        data.close()
    print(dict)

#Создаём файл если нет
def creating_file():
    file = 'Phonebook.txt'
    with open (file, 'w', encoding= 'utf-8') as data:
        data.write('Номер по списку; Фамилия; Имя; Номер телефона; Комментарий: \n')

#Открываем весь файл
def open_file(file):
    #file = 'Phonebook.txt'
    with open(file, 'r', encoding='utf-8') as data:
        res = data.read()
        print(res)
    return res

#Поиск по файлу
def search_file(file):
    #file = 'Phonebook.txt'
    with open(file, 'r', encoding='utf-8') as data:
        res = data.readline()
        for line in res:
            print(line.strip())
        data.close()
    return res



#Поиск по списку контактов
# def search_contact():
#     body = []
#     with open("file.txt", encoding='utf-8') as thisfile:
#         i = 0
#         body = thisfile.readlines()
 
#     with open("fileS.txt", 'w', encoding='utf-8') as new_file:
#         for line in body:
#             list = line.rstrip("\n").split(" ")
#             i=i+1
#             print (list)
#         for word in list:
#             if word == "мрй":
#                 list.remove("мрй")
#             myString = ' '.join(list)
#         print(myString)
            #####new_file.write("{}\n".format(myString))

def export_data():
    with open('file.txt', 'r',  encoding='utf-8') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split()
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split()
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split()
                data.append(temp)
            elif line != '':
                if line != '\n':
                   t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data 

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

search_data("арт", export_data())
    # parse_string = search_file('Phonebook.txt')
    # str = input()
    # sub_string = str
    # with open("file.txt") as file:
    #     lines = file.readlines()
    # for line in lines:
    #     if sub_string == '2':
    #         #if sub_string in line:
    #         print(line)
    #     else:
    #         break

    #print(parse_string)
#     my_dict = {}
#     with open('file.txt') as file:
#         for line in file.readlines():
#             name, value = line.split(':')
#     my_dict[name.strip()] = value.strip()
# # code

#     with open('file.txt', 'w') as file:
#         file.writelines([f'{name} : {value}\n' for name, value in my_dict.items()])


#Проверка
#creating_file()        
#input_data()


