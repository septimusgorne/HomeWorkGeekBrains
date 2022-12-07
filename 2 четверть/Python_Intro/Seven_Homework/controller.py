# from import_data import export_data
from export_data import export_data
#from print_data import print_data
from search_data import search_data

def greeting():
    print("Здрасти")

def inpud_data():
    last_name = input('Введите фамилию: ')
    firs_name = input('Введите имя: ')
    phone_number = input('Введите телефон: ')
    note = input('Введите коммент: ')
    return [last_name, firs_name, phone_number, note]

def choice_sep():
    sep = input('Введите разделитель: ')
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print('Выберите действие: \n\
    1 - Import \n\
    2 - Export \n\
    3 - Search ')
    ch = input('Введите цифру: ')
    if ch == 1:
        sep = choice_sep()
        #import_data(inpud_data(), sep)
    elif ch == 2:
        data = export_data
    else:
        word = input('Введите данные для поиска: ')
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print('Фамилия'.center(20), "Имя".center(20), 'Телефон'.center(15), 'Комментарий'.center(30))
            print("-"*85)
            print(item[0].center(20), item[1].center(20), item[2].center(15), item[3].center(30))
        else:
            print("Данные не обнаружены")
    



