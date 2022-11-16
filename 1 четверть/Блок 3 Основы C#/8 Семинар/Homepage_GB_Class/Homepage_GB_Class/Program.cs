using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Homepage_GB_Class
{
    internal class Program
    {
        static void Main()
        {
            int numb;
            Console.WriteLine("\nВведите номер задачи от 1 до 5");
            int.TryParse(Console.ReadLine(), out numb);

            switch(numb)
            {
                case 1:
                    Console.WriteLine("<Задача 54. Сортировка по убыванию построчно элементов двумерного массива>, нажмите Enter");
                    if (Console.ReadKey().Key == ConsoleKey.Enter)
                        Part_54.Resolved_54();
                    else
                        goto defaut;
                    break;
                case 2:
                    Console.WriteLine("<Задача 56. В прямоугольный двумерном массиве, необходимо найти строку с наименьшей суммой элементов>,\n нажмите Enter");
                    if (Console.ReadKey().Key == ConsoleKey.Enter)
                        Part_56.Resolved_56();
                    else
                        goto defaut;
                    break;
                case 3:
                    Console.WriteLine("Задача 58. Произведение двух матриц, нажмите Enter");
                    if (Console.ReadKey().Key == ConsoleKey.Enter)
                        Part_58.Resolved_58();
                    else
                        goto defaut;
                    break;
                case 4:
                    Console.WriteLine("Задача 60.  трёхмерный массив из неповторяющихся двузначных чисел, построчный вывод массива, прибавляя индексы каждого элемента, нажмите Enter");
                    if (Console.ReadKey().Key == ConsoleKey.Enter)
                        Part_60.Resolved_60();
                    else
                        goto defaut;
                    break;
                case 5:
                    Console.WriteLine("Задача 60.Программу, которая заполняет спирально массив 4 на 4, нажмите Enter");
                    if (Console.ReadKey().Key == ConsoleKey.Enter)
                        Part_62.Resolved_62();
                    else
                        goto defaut;
                    break;
                defaut:
                    Main();
                    break;
            }

        }
    }
}
