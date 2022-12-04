#Программа удаляющая из текста слова содержащие "абв":

import random
list_word = ["за", "ма", "ба", "ка", "бв", "ша", "ах"]
text = list(map(lambda x: "".join(random.sample(list_word, 2)), range(random.randint(12,15))))
print(f'text: {" ".join(text)}')
#print(*text)
input_text = list(x for x in text if "абв" not in x)
print(f'Результат: {" ".join(input_text)}')
