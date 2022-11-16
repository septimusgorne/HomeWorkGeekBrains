//1 Вариант
using System;
using System.Linq;

namespace Unique_Elements_Array
{
    class Program
    {
        public static void Main(String[] args)
        {
            Console.Write("Введите число элементов массива: \t");
            var N = Console.ReadLine();
            int numb;

            var isNumber = int.TryParse(N, out numb);
            if (isNumber == false)
            {
                Console.WriteLine("Введите целое число");
                Main(args);
            }
            else
            {
                Unique_Arr(numb);
            }
        }
        private static void Unique_Arr(int numb)
        {
            int[] myArr = new int[numb];

            for (int i = 0; i < myArr.Length; i++)
            {
                Console.Write($"Введите элемент индекса {i}: \t"); ;
                myArr[i] = int.Parse(Console.ReadLine());
            }

            Console.Write("\nУникальные элементы массива: ");
            foreach (var uniq in myArr.Distinct<int>())
            {
                Console.Write("\n{0}", uniq);
            }
            Console.ReadKey();
        }
    }
}

