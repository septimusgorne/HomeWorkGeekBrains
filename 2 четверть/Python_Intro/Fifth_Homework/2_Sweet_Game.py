# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

def inputs():
    rand = int(input("Введите количество конфет от 1 до 28:  "))
    sum = 0
    while True:
        if rand >= 1 and rand <= 28:
            sum += rand
            return sum
        else:
            print("\n!!!!!!Игра начинается сначала!!!!!!!!\n")
            main(2021-sum)
    return rand
        
def main(rester = 20):
    user_1, user_2 = "Игрок 1", "Игрок 2"
    #current_user = user_1 
    current_user = random.choice([user_1, user_2]) 
    bot = user_2
    #rester = 2021
    while rester > 0:
        if current_user == bot:####Условие для бота
                delSweet = random.randint(1, 28)
        else:
            delSweet = inputs()
        rester = rester - delSweet
        
        print(f'Ход игрока: {current_user}')
        print(f'Количество взятых конфет {delSweet}  Количество оставшихся конфет: {rester}')
        
        current_user = user_2 if current_user == user_1 else user_1
    if rester >= 1 and rester <= 28:
        print('Победил {}'.format(current_user))
    return rester

gow = main()
print(gow)