# 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""



# count_of_sticks = int(input('введите количество палочек для игры: '))
# gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
# current_gamer = gamer_1
# while count_of_sticks > 0:
#     print('количество оставшихся палочек: {}'.format(count_of_sticks))
#     while True:
#         number_to_delete = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
#         if number_to_delete >= 1 and number_to_delete <= 3:
#             break
#     count_of_sticks -= number_to_delete
#     current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

# print('Победил {}'.format(current_gamer))

# box_sweet = 2021
# user_1, user_2  = "Первый игрок", "Второй игрок"
# current_user = user_1
# rand = random.randint(5, 23)

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