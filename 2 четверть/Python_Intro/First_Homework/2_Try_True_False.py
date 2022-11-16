#1.Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def InputNumbers(x):
    inputData = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f'Введите значение {inputData[i]}:'))
    return a

def TryTrueFalse(x):
    part_1 = not(x[0] or x[1] or x[2])
    part_2 = not x[0] and not x[1] and not x[2]
    return part_1 == part_2

if TryTrueFalse(InputNumbers(3)) == True:
    print(True)
else:
    print(False)

