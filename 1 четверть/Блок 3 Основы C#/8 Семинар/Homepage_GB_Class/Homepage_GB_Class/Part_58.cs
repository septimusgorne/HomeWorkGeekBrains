using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
namespace Homepage_GB_Class
{
    public class Part_58
    {
        public static void Resolved_58()
        {
            Console.Clear();

            Console.WriteLine($"\nВведите размер матриц, значения заполнятся рандомно:");

            int oneRange = InputNumbers("Введите число строк 1-й матрицы: ");
            int twoRange = InputNumbers("Введите число столбцов 1-й матрицы (и строк 2-й): ");
            int threeRange = InputNumbers("Введите число столбцов 2-й матрицы: ");

            int[,] firstMartrix = new int[oneRange, twoRange];
            CreateArray(firstMartrix);
            Console.WriteLine($"\nПервая матрица:");
            WriteArray(firstMartrix);

            int[,] secomdMartrix = new int[twoRange, threeRange];
            CreateArray(secomdMartrix);
            Console.WriteLine($"\nВторая матрица:");
            WriteArray(secomdMartrix);

            int[,] resultMatrix = new int[oneRange, threeRange];

            MultiplyMatrix(firstMartrix, secomdMartrix, resultMatrix);
            Console.WriteLine($"\nПроизведение первой и второй матриц:");
            WriteArray(resultMatrix);
        }
           static void MultiplyMatrix(int[,] firstMartrix, int[,] secomdMartrix, int[,] resultMatrix)
            {
                for (int i = 0; i < resultMatrix.GetLength(0); i++)
                {
                    for (int j = 0; j < resultMatrix.GetLength(1); j++)
                    {
                        int sum = 0;
                        for (int k = 0; k < firstMartrix.GetLength(1); k++)
                        {
                            sum += firstMartrix[i, k] * secomdMartrix[k, j];
                        }
                        resultMatrix[i, j] = sum;
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
