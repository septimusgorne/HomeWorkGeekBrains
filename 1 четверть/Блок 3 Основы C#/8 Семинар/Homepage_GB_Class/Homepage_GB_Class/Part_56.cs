using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
namespace Homepage_GB_Class
{
    public class Part_56
    {
        public static void Resolved_56()
        {
            Console.Clear();

            Console.WriteLine($"\nВведите размер массива, значения заполнятся рандомно:");

            int cols = InputNumbers("Введите число строк: ");
            int rows = InputNumbers("Введите число стобцов: ");

            int[,] array = new int[cols, rows];
            CreateArray(array);
            WriteArray(array);

            int minSumLine = 0;
            int sumLine = SumLineElements(array, 0);
            for (int i = 1; i < array.GetLength(0); i++)
            {
                int tempSumLine = SumLineElements(array, i);
                if (sumLine > tempSumLine)
                {
                    sumLine = tempSumLine;
                    minSumLine = i;
                }
            }

            Console.WriteLine($"\n{minSumLine + 1} - строкa с наименьшей суммой ({sumLine}) элементов ");
        }

        static int SumLineElements(int[,] array, int i)
        {
            int sumLine = array[i, 0];
            for (int j = 1; j < array.GetLength(1); j++)
            {
                sumLine += array[i, j];
            }
            return sumLine;
        }

        static int InputNumbers(string input)
        {
            Console.Write(input);
            int output = Convert.ToInt32(Console.ReadLine());
            return output;
        }

        static void CreateArray(int[,] array)
        {
            Random random = new Random();
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    array[i, j] = random.Next(0, 100);
                }
            }
        }
        static void WriteArray(int[,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write(array[i, j] + " ");
                }
                    Console.WriteLine();
                }
            }
    }
}
