def initial():
    n = input('Поиск 1 запись 2')
    if n == '1':
        search()
    else:
        view_read()

def view_read():#read file
    l = ['Фамилия', 'Имя', 'Телефон', 'Комментарии']
    data = []
    flag = input('Выберите формат файла txt csv')
    for i in range(len(l)):
        data.append(input(l[i]))
    return flag, data
def search():#search data
    n = input()
    return 'search', n