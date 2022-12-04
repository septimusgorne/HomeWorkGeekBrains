# Задача про 2021 конфету:

import random

#Проверяем количество конфет
def ask(min, max):
    candy = int(input("Сколько конфет ты берешь?"))
    while candy > max or candy < min:
        print("Возьми меньше 28 конфет!")
    return candy
#Бот берет конфеты
def bot_func(min, max):
    candy = random.randint(min, max + 1)
    print(f'{bot}, взял {candy} конфет')
    return candy

text = "На столе лежит 2021 конфета\n\
2 игрока по очереди берут конфеты\n\
Проиграет тот кому останется взять последние конфеты"
print(text)

#Вводимые данные:
candies = 221#2021
max = 28
min = 1
bot = "Bot"

man = input("Введите свое имя:")
lot = random.choice([man, bot])
if lot == bot:
    print(f'Первый игрок: {lot}')
else:
    print(f'{man}, ты первый игрок')

while candies > 1:
    if lot == bot:
        candies -= bot_func(min, max)
        if candies < 0:
            break
        print(f'{candies} candies left')
        lot = man 
    else:
        candies -= ask(min, max)
        if candies < 0:
            break

#Проигрыш
print(f'{lot}, проиграл , {candies} конфет ')