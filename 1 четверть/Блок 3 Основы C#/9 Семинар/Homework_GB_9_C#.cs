using System;


namespace Homework_GB_9
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Введите номер задачи от 1 до 3х");
            int n = int.Parse(Console.ReadLine());
            switch(n)
            {
                case 1:
                    Console.WriteLine("Введите N");
                    RecursionNumber(int.Parse(Console.ReadLine()));//Задача 64. Рекурсия, вывод всех натуральных чисел
                    break;
                case 2:
                    Console.WriteLine("Сумма чисел между M и N");//Задача 66. Задайте значения M и N.Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
                    SumBetweenNM();
                    break;
                case 3:
                    Console.WriteLine("Аккерман рекурсия, введите M и N");//Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n
                    Console.WriteLine("Результат: " + AkkermanFunction(uint.Parse(Console.ReadLine()), uint.Parse(Console.ReadLine())));    
                    break;
                default:
                    break;

            }
        }
        static void RecursionNumber(int N)
        {
            if (N != 0)
                Console.Write(" " + N);
                RecursionNumber(N - 1);
        }
        static void SumBetweenNM()
        {

            Console.Write("Введи N: ");
            int N = Convert.ToInt16(Console.ReadLine());

            Console.Write("Введи M: ");
            int M = Convert.ToInt16(Console.ReadLine());

            int sum = 0;
            Console.WriteLine($"N={N}, M={M}");

            for (int i = N; i <= M; i++)
            {
                sum = sum + i;
            }
            Console.Write("\nСумма чисел: " + sum);
            Console.ReadLine();
        }


        static uint AkkermanFunction(uint n, uint m)
        {
            if (n == 0)
                return m + 1;
            else
              if ((n != 0) && (m == 0))
                return AkkermanFunction(n - 1, 1);
            else 
               return AkkermanFunction(n - 1, AkkermanFunction(n, m - 1));
        }
    }
}
