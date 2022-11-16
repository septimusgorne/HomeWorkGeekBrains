#2.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

print("Введите значение X точки A")
xA = int(input())
print("Введите значение Y точки A")
yA = int(input())
print("Введите значение X точки B")
xB = int(input())
print("Введите значение Y точки B")
yB = int(input())
coordinate_2Point = [(xA, yA), (xB, yB)]

def distance(coordinate_Point):
    return((((xB) - (xA)) ** 2 + ((yB) - (yA)) ** 2) ** 0.5)

dist = distance(coordinate_2Point)
print(round(dist, 3))
