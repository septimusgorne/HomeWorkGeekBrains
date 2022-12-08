import schoolchild_info as si
import cabinet_info as cab


def option():
    print("\nВас приветствует Электронный дневник")
    ch = int(input('Выберите действие: \n \
    1: Поиск ID школьника по фамилии \n \
    2: Посмотреть класс и место, которое занимает школьник \n \
    3: Выход\n \
    Вы выбрали: '))

    if ch == 1:
        Surn = str(input("Введите фамилию ученика: "))
        if Surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surn)
        print(f"{si.stud_card['ID'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Фамилия'][index]}\n,{si.stud_card['Дата рождения'][index]}, {si.stud_card['Успеваемость'][index]}")
        print('\nВы хотите выполнить другую операцию? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID студента для вывода по классам: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}\n\, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, Фамилия - {si.stud_card['Фамилия'][index]}, и успеваемасть у ученика: {si.stud_card['Успеваемость'][index]}")
            print('\nВы хотите выполнить другую операцию? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()