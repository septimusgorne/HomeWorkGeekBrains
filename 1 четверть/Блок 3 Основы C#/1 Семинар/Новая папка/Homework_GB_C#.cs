using System;
using System.Collections.Generic;
using System.Linq;

namespace Homework_GB
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //2_Max_Two_Numbers
            
            /*
            int num1, num2;
            Console.WriteLine("Введите первое число: ");
            int.TryParse(Console.ReadLine(), out num1);

            Console.WriteLine("Введите второе число: ");
            int.TryParse(Console.ReadLine(), out num2);

            int res = num1 > num2 ? num1 : num2;
            Console.WriteLine($"Наибольшее число равно: \n{res}");
            Console.ReadLine();
            */

            //---------------------------------------------------------
            //---------------------------------------------------------

            //4_Max_Three_Numbers

            /*
            int num1, num2, num3, res;
            Console.WriteLine("Введите первое число: ");
            int.TryParse(Console.ReadLine(), out num1);

            Console.WriteLine("Введите второе число: ");
            int.TryParse(Console.ReadLine(), out num2);

            Console.WriteLine("Введите второе число: ");
            int.TryParse(Console.ReadLine(), out num3);

            Console.WriteLine("Наибольшее число: ");
            res = new[] { num1, num2, num3 }.Max(); 
            
            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            //res = num2 > num1 ? num2 : num1;
            //res = num3 > res ? num3 : res;
            
            Console.WriteLine(res);
            Console.ReadLine();
            */

            //---------------------------------------------------------
            //---------------------------------------------------------

            //6_Even

            /*
            int N;
            Console.WriteLine("Введите число для проверки: ");
            int.TryParse(Console.ReadLine(), out N);
            if (N % 2 == 0)
                Console.WriteLine("Чётное");
            else
                Console.WriteLine("Нечётное");
            Console.ReadLine();
            */

            //---------------------------------------------------------
            //---------------------------------------------------------

            //8_Even_Print(applied List<>, LINQ, IEnumerable)

            /*
            int N;
            int i = 0;
            Console.WriteLine("Введите конечное число: ");
            int.TryParse(Console.ReadLine(), out N);
            while(N > 0)
            {
                i++;
                if(i % 2 ==0)
                {
                    Console.WriteLine($"Чётное число: {i}");
                }
                N--;
            }
            */

            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            /*
            int N;
            int x = 1;
            Console.WriteLine("Введите количество элементов коллекции: ");
            int.TryParse(Console.ReadLine(), out N);
            List<int> arr = new List<int>();
   
            for (int i = 0; i < N; i++)
            {
                arr.Add(x);
                x++;
            }

            IEnumerable<int> result = arr.Where(a => a % 2 == 0);
            Console.WriteLine("Чётные элементы массива: ");
            foreach (var item in result)
            {
                Console.WriteLine($"Чётное число: {item}");
            }
            */

            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            /*
            int N;
            Console.WriteLine("Введите конечное число: ");
            int.TryParse(Console.ReadLine(), out N);
            
            Stack<int> stack = new Stack<int>(N);
            for (int i = 0; i <= N; stack.Push(i++));

            Stack<int> Event = new Stack<int>(stack.Count / 2);
            foreach (var item in stack)
            {
                if(item % 2 == 0 && item != 0)
                {
                    Event.Push(item);   
                }
            }
            Console.WriteLine("Чётные числа: ");
            foreach (var item in Event)
            {
                Console.WriteLine(item + " ");
            }
            */

            //---------------------------------------------------------
        }
    }
}
