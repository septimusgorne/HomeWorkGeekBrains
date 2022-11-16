
using System;
using System.Linq;
using System.Collections.Generic;

namespace GB_6
{
    class Program
    {
        public static void Main()
        {
            int num;
            Console.WriteLine("Выберите номер задачи от 1 до 2х");
            int.TryParse(Console.ReadLine(), out num);
            switch (num)
            {
                case 1:
                    int num2;
                    Console.WriteLine("Выберите 1 или 2 вариант решения");
                    int.TryParse(Console.ReadLine(), out num2);
                    if (num2 == 1)
                        Equals();
                    else if (num2 == 2)
                        CountIndexMoreNullLINQ();
                    break;
                    CountIndexMoreNull();
                    break;
                case 2:
                    int num3;
                    Console.WriteLine("Выберите 1 или 2 вариант решения");
                    int.TryParse(Console.ReadLine(), out num3);
                    if (num3 == 1)
                        Equals();
                    else if (num3 == 2)
                        Console.WriteLine("Второй вариант");
                    InputDatePoint();
                    break;
                default:
                    Main();
                    break;
            }
        }

        static void CountIndexMoreNull()
        {
            Console.WriteLine("/Нахождение количества элементов больше 0 в рандомном массиве/");
            int countArray;
            Console.WriteLine("\nВведите число элементов массива");
            int.TryParse(Console.ReadLine(), out countArray);
            int[] arr = new int[countArray];
            int sumIndexMoreNull = 0;

            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = new Random().Next(-20, 100);
                Console.Write(" " + arr[i]);
                if (arr[i] > 0)
                {
                    sumIndexMoreNull++;
                }
            }
            Console.WriteLine($"\nКоличество элементов массива: {sumIndexMoreNull}");

        }

        static void CountIndexMoreNullLINQ()
        {
            Console.WriteLine("/Нахождение количества элементов больше 0 в рандомном массиве (LINQ)/");

            Random _rand = new Random();
            List<int> result = new List<int>();

            Console.Write("Введите размер списка: ");
            int N = int.Parse(Console.ReadLine());

            Console.WriteLine("Введите элементы списка");
            for (int i = 0; i < N; i++)
            {
                Console.Write($"Элемент {i} :");
                result.Add(int.Parse(Console.ReadLine()));
            }
            Console.WriteLine("Список введённых элементов: ");
            foreach (var print in result)
            {
                Console.Write(" " + print);
            }

            // Вывод количества значений больше 0
            var sum = result.Where((cat, index) => cat > 0)
                                    .Select(index => index)
                                    .Count();
            Console.WriteLine($"\nКоличество элементов больше 0: {sum}");

        }

        static void Equals()
        {
            Console.WriteLine("/Нахождение точек пересечения прямых/");
            float k1, b1;
            float k2, b2;

            float x, y;
            Console.WriteLine("Введите значение b1:");
            float.TryParse(Console.ReadLine(), out b1);

            Console.WriteLine("Введите значение k1:");
            float.TryParse(Console.ReadLine(), out k1);

            Console.WriteLine("Введите значение b2:");
            float.TryParse(Console.ReadLine(), out b2);

            Console.WriteLine("Введите значение k2:");
            float.TryParse(Console.ReadLine(), out k2);


            if ((k1 == k2) && (b1 == b2))
            {
                Console.WriteLine("Линии совпадают");
            }
            else if (k1 == k2)
            {
                Console.WriteLine("Линии параллельны");
            }
            else
            {
                x = (b2 - b1) / (k1 - k2);
                y = (k1 * (b2 - b1)) / (k1 - k2) + b1;
                Console.WriteLine($"Прямые пересекаются в точках X: {x} Y: {y}");
            }
            Console.ReadLine();
        }

        //2 Вариант решения 2й задачи ----------------------------------------------
        static public Point ResolvePoint(Point A, Point B)
        {
            float x = (B.B - A.B) / (A.K - B.K);
            float y = (A.K * (B.B - A.B)) / (A.K - B.K) + A.B;

            return new Point(x, y);
        }

        static void InputDatePoint()
        {
            Console.WriteLine("/Нахождение точек пересечения прямых/");
            float b1, k1, b2, k2;

            Console.WriteLine("Введите значение b1:");
            float.TryParse(Console.ReadLine(), out b1);

            Console.WriteLine("Введите значение k1:");
            float.TryParse(Console.ReadLine(), out k1);

            Console.WriteLine("Введите значение b2:");
            float.TryParse(Console.ReadLine(), out b2);

            Console.WriteLine("Введите значение k2:");
            float.TryParse(Console.ReadLine(), out k2);

            Point A = new Point(b1, k1);
            Point B = new Point(b2, k2);

            Point P = ResolvePoint(A, B);

            Console.WriteLine("Точка пересечения X: {0}  Y: {1}", P.B, P.K);
            Console.ReadKey();
        }
    }

    class Point
    {
        public float B { get; set; }
        public float K { get; set; }
        public Point() { }
        public Point(float b, float k)
        {
            B = b;
            K = k;
        }
    }
    //------------------------------------------------------

}
