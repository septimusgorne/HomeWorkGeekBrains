using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Remoting.Metadata.W3cXsd2001;

namespace Homework_GB_7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            TwoRangArrayRandom();//Задача 47.Массив случайных значений
            ReturnStateElement();//Задача 50.Поиск элемента в массиве по координатам
            SearchAverageArray();//Задача 52.Среднее арифмет. элементов столбца
        }

        //Задача 47.Массив случайных значений
        static void TwoRangArrayRandom()
        {
            Console.WriteLine("Введите m");
            int n = int.Parse(Console.ReadLine());

            Console.WriteLine("Введите n");
            int m = int.Parse(Console.ReadLine());

            int[,] a = new int[n, m];
            Random random = new Random();

            for (int i = 0; i < n; i++)

                for (int j = 0; j < m; j++)
                {
                    a[i, j] = random.Next(0, 100);
                }

            Console.WriteLine("Массив случайных значений");
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine();
                for (int j = 0; j < m; j++)
                {
                    Console.Write("{0}\t", a[i, j]);
                }
            }
            Console.ReadKey();
        }

        //Задача 50.Поиск элемента в массиве по координатам
        static void ReturnStateElement()
        {
            int n, m;
            Console.WriteLine("Введите n");
            int.TryParse(Console.ReadLine(), out n);

            Console.WriteLine("Введите m");
            int.TryParse(Console.ReadLine(), out m);
            Random random = new Random();

            int[,] array = new int[m, n];

            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                    array[i, j] = random.Next(0, 21);
            }

            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                    Console.Write(array[i, j] + "\t  ");
                Console.WriteLine();
            }

            Console.WriteLine("Введите n для поиска элемента");
            int x = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Введите m для поиска элемента");
            int y = Convert.ToInt32(Console.ReadLine());

            if (x > m && y > n)
                Console.WriteLine("такого числа в массиве нет");
            else
            {
                var res = array.GetValue(x, y);
                Console.WriteLine("Это элемент: " + res);
            }

        }

        //Задача 52.Среднее арифмет. элементов столбца
        static void SearchAverageArray()
        {
            int cols, rows;
            int n, m;

            Console.WriteLine("Задайте количество столбцов");
            int.TryParse(Console.ReadLine(), out rows);

            Console.WriteLine("Задайте количество строк");
            int.TryParse(Console.ReadLine(), out cols);

            int[,] arr = new int[cols, rows];

            for (int i = 0; i < cols; i++)

                for (int j = 0; j < rows; j++)
                {
                    Console.WriteLine($"Введите элемент столбца {i} строки {j}");
                    arr[i, j] = int.Parse(Console.ReadLine());
                }

            for (int i = 0; i < rows; i++)
            {
                int res = 0;
                for (int t = 0; t < cols; t++)
                {
                    res += arr[t, i];
                }
                Console.WriteLine($"Cреднее арифметическое элементов столбца {i + 1} = {(float)res / 3}");
            }
        }
    }
}
