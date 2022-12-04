
#Поиск и вывод уникальных чисел:

enum_number = list(map(int, input('Введите числа: ').split()))
enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))
print(enum_number, 'Уникальные числа ->', enum_unique)

#Программа удаляющая из текста слова содержащие "абв":

# import random
# list_word = ["за", "ма", "ба", "ка", "бв", "ша", "ах"]
# text = list(map(lambda x: "".join(random.sample(list_word, 2)), range(random.randint(12,15))))
# print(f'text: {" ".join(text)}')
# input_text = list(x for x in text if "абв" not in x)
# print(f'Результат: {" ".join(input_text)}')

