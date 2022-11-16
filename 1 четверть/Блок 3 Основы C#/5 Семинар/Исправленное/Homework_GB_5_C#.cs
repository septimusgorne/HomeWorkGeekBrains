using System;
using System.Collections.Generic;//для 3го варианта решения 3й задачи и 2го варианта 2й задачи
using System.Linq;//для 3го варианта решения 3й задачи и 2го варианта 2й задачи

namespace GB_5
{
    class Program
    {
        public static void Main()
        {
            Console.WriteLine("Выберите задачу от 1 до 3х");
            int num;
            int.TryParse(Console.ReadLine(), out num);
            switch(num)
            { 
                    case(1):
                    Arr_Random();//Задача 34. Массив случайных положительных трёхзначных чисел
                    Main();
                    break;

                    case(2):
                    Arr_Random_Sum();//Задача 36 одномерный массив случайных чисел, нахождение суммы элементов
                    Main();
                    break;

                    case(3):
                    Delta_Sort_Random();//Задача 38: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
                    Main();
                    break ;

                    default:
                    Main();
                    break ;
            }

            Arr_Random_Sum();
        }

        //Задача 34. Массив случайных положительных трёхзначных чисел
        static void Arr_Random()
        {
            Console.WriteLine("Задача 34. Массив случайных элементов");

            Random rnd = new Random();
            int[] arr = new int[rnd.Next(3, 10)];

            Console.WriteLine("\n Вывод массива");
            for (int i = 0; i < arr.Length; i++)
            {
                int val = rnd.Next(100, 999);
                arr[i] = val;
                Console.Write(" " + arr[i]);
            }
            Console.ReadLine();
        }

        //Задача 36 одномерный массив случайных чисел, нахождение суммы элементов
        static void Arr_Random_Sum()
        {
            Console.WriteLine("Массив случайных элементов и их сумма");

            /*
            Random rnd = new Random();
            int[] arr = new int[rnd.Next(3, 10)];
            int sum = 0;

            for (int i = 0; i < arr.Length; i++)
            {
                int val = rnd.Next(-100, 100);
                arr[i] = val;

                if (i % 2 != 0)
                {
                    sum += arr[i];
                }
                Console.Write(" " + arr[i]);
            }
            Console.WriteLine($"\nСумма элементов на нечетных позициях: {sum}");
            Console.ReadLine();
            */


            //or that

            Random _rand = new Random();
            List<int> result = Enumerable.Range(1,  _rand.Next(4, 10))
                                    .Select(x => _rand.Next(10))
                                    .ToList();
            //Вывод массива случайных элементов
            foreach (var print in result)
            {
                Console.Write(" " + print);
            }
            //Суммируем элементы под нечётными индексами
            var sum = result.Where((cat, index) => index % 2 != 0).Sum();
            Console.WriteLine($"\nСумма элементов нечетных чисел = {sum}");
        }

        //Задача 38. Массив вещественных случайных чисел, разница между макс. и мин. элементами

        static void Delta_Sort_Random()
        {
            Console.WriteLine("Массив случайных элементов, разница между макс. и мин. элементами");

            /*Random random = new Random();
            int[] array = new int[random.Next(3, 10)];
            int min = int.MaxValue;
            int max = int.MinValue;
            int temp = 0;
            for (int i = 0; i < array.Length; i++)
            {
                temp = random.Next(-99, 99);
                array[i] = temp;
                if (array[i] < min)
                    min = array[i];
                if (array[i] > max)
                    max = array[i];
            }

            Console.WriteLine("Массив случайных элементов");
            foreach (var item in array)
            {
                Console.Write(" " + item);
            }
            int delta = max - min;

            Console.WriteLine($"\nМинимальное значение:{min}");
            Console.WriteLine($"Максимальное значение:{max}");
            Console.WriteLine($"Разница между max и min значениями:{delta}");

            Console.ReadLine();*/


            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            /*
            Random rnd = new Random();
            int[] arr = new int[rnd.Next(3, 10)];
            int min = 0;
            int max = 0; 
            int temp = 0;
            int delta = 0;
          
            Console.WriteLine("\nВывод массива случайных элементов");
            for (int i = 0; i < arr.Length; i++)
            {
                int val = rnd.Next(-99, 99);
                arr[i] = val;
                Console.Write(" " + arr[i]);
            }

            //Сортировка пузырьком
            Console.WriteLine("\nСортированный массив");
            for (int i = 0; i < arr.Length; i++)
            {
                for (int j = i + 1; j < arr.Length; j++)
                {
                    if (arr[i] > arr[j])
                    {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                    min = arr[0];
                    max = arr[j];
                    delta = Math.Abs(min - max);
                }

                Console.Write(" " + arr[i]);
            }
            Console.WriteLine($"\nРазница между max: {max} и min :{min} Результат: {delta}");
            Console.ReadLine();
            */

            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            //Создание случайного массива случайной длины диапазона
            Random _rand = new Random();
            List<int> result = Enumerable.Range(1,  _rand.Next(4, 10))
                                    .Select(x => _rand.Next(10))
                                    .ToList();
            //Вывод массива случайных элементов
            foreach (var print in result)
            {
                Console.Write(" " + print);
            }

            //Сортировка
            var sort = result.OrderBy(x => x).ToList();

            //Вывод сортировки
            foreach (var print in sort)
            {
                Console.Write($"\t\n {print}");
            }
            //Вывод разницы
            Console.WriteLine($"\nРазница между MAX: {sort.Max()} и MIN: {sort.Min()} : \n{sort.Max() - sort.Min()}");
            //P.S расписал для наглядности пошагово

        }
    }
}