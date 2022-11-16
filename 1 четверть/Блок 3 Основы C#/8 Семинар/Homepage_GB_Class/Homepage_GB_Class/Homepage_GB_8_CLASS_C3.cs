using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Заполнение массива спирально
namespace Homepage_GB_Class
{
    public class Part_62
    {
        public static void Resolved_62()
        {
            Console.Clear();

            int n = 4;
            int[,] sqareMatrix = new int[n, n];

            int temp = 1;
            int i = 0;
            int j = 0;

            while (temp <= sqareMatrix.GetLength(0) * sqareMatrix.GetLength(1))
            {
                sqareMatrix[i, j] = temp;
                temp++;
                if (i <= j + 1 && i + j < sqareMatrix.GetLength(1) - 1)
                    j++;
                else if (i < j && i + j >= sqareMatrix.GetLength(0) - 1)
                    i++;
                else if (i >= j && i + j > sqareMatrix.GetLength(1) - 1)
                    j--;
                else
                    i--;
            }

            WriteArray(sqareMatrix);
        }

          static void WriteArray(int[,] array)
            {
                for (int i = 0; i < array.GetLength(0); i++)
                {
                    for (int j = 0; j < array.GetLength(1); j++)
                    {
                        if (array[i, j] / 10 <= 0)
                            Console.Write($" {array[i, j]} ");

                        else Console.Write($"{array[i, j]} ");
                    }
                    Console.WriteLine();
                }
          }
    }
}