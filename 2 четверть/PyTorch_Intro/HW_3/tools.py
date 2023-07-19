from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from multiprocessing import cpu_count


def ar_split_eq_cpu(a, n=0):
    """Разделяет массив на приблизительно равные части
    :params a: массив
    :params n: кол-во частей для разделения.
               Если не указано, торавно кол-ву CPU-1
    
    Пример: ar_split(range(11), 3) вернёт
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10]]
    """
    if not n:
        n = cpu_count() - 1 if cpu_count() > 1 else 1 
        
    k, m = divmod(len(a), n)
    res = [a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n)]
    res = [i for i in res if i != []]
    return res


def paralell_execution(func, arg, cpu_cnt=0, method=''):
    """Запускает параллельные вычисления разными способами.
    :params func: функция, которую будут вызывать параллельно
    :params list arg: аргументы для функции
    :params int cpu_count: Количество CPU для расчётов
    :params str method: Выбор способа разделения задач по процессорам:
        multithreading - годится для задач, где нужно ждать. К примеру,
        параллельная загрузка файлов.
        multiprocessing - годится для задач, где нужна вычислительная
        мощность всех ядер.
        Экспериментально установлено: multiprocessing будет выигрывать
        multithreading только на больших объёмах расчётов и большом
        количестве CPU (6+). В противном случае multithreading будет
        слегка быстрее.
    :return list: список возвращённых значений от функций func,
                  которые были запущены параллельно. Порядок
                  элементов не соответствует порядку запуска,
                  все элементы будут перемешаны!
    """
    res = None
    
    # способ параллельной обработки
    if not len(method):
        if cpu_cnt < 6:
            method = 'multithreading'
        else:
            method = 'multiprocessing'
            
    # кол-во ядер для обработки
    # в многоядерной системе одно ядро резервируем для работы системы
    if not cpu_cnt:
        cpu_cnt = cpu_count() - 1 if cpu_count() > 1 else 1 

    # Если процессоров меньше, чем задач, то разбиваем аргументы
    # на примерно равные группы для параллелизации
    if cpu_cnt < len(arg):
        arg = ar_split_eq_cpu(arg, cpu_cnt)
    
    # запускаем параллельные вычисления
    if method == 'multiprocessing':
        with ProcessPoolExecutor(cpu_cnt) as ex:
            res = ex.map(func, arg)

    if method == 'multithreading':
        with ThreadPoolExecutor(cpu_cnt) as ex:
            res = ex.map(func, arg)
    
    # Преобразование list(res) запускает весь процесс подсчёта!
    # Если нужно запустить принудительно ранее, то можно заменить
    # map на submit и выполнить метод res.result()
    res = list(res)

    # на этом моменте все параллелные расчёты закончились и 
    # результаты объединились в массив res. Теперь надо
    # проверить, что в этом массиве столько результатов,
    # сколько потоков запускали.
    assert len(arg) == len(res), \
            'Во время расчётов была была утеряна часть данных! ' \
            'Некоторые потоки программы не вернули свой результат!'
    
    return list(res)