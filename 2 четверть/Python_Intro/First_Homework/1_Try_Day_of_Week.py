# #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def TryTypeDate(inputData):
    isNumber = False
    while not isNumber:
        try:
            number = int(input(f"{inputData}"))
            isNumber = True
        except ValueError:
            print("Введите число дня недели:")
    return number

def checkNumber(numbDayOfWeek):
    if 0 < numbDayOfWeek < 6:
        print("Рабочий день")
    elif 6 <= numbDayOfWeek <= 7:
        print("Выходной")
    else:
        print("Дня недели не существует")

numbDayOfWeek = TryTypeDate("Введите число дня недели:")
checkNumber(numbDayOfWeek)