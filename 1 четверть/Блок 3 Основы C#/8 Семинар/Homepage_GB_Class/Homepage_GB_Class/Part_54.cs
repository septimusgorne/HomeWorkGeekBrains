using System;
using System.Collections.Generic;
using System.Linq;

//Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.

namespace Homepage_GB_Class
{
    public class Part_54
    {
        public static void Resolved_54()
        {
            Console.WriteLine("Решение задачи 54");

            Console.Clear();

            Console.WriteLine($"\nВведите размер массива, значения заполнятся рандомно:");
            int cols = InputNumbers("Введите число строк: ");
            int rows = InputNumbers("Введите число стобцов: ");

            int[,] array = new int[cols, rows];
            CreateArray(array);

            Console.WriteLine("\nНесортированный массив");
            WriteArray(array);

            Console.WriteLine($"\nСортированный массив: ");
            OrderArrayLines(array);
            WriteArray(array);
        }

        static void OrderArrayLines(int[,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    for (int k = 0; k < array.GetLength(1) - 1; k++)
                    {
                        if (array[i, k] < array[i, k + 1])
                        {
                            int temp = array[i, k + 1];
                            array[i, k + 1] = array[i, k];
                            array[i, k] = temp;
                        }
                    }
                }
            }
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
                    array[i, j] = random.Next(0, 10);
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
