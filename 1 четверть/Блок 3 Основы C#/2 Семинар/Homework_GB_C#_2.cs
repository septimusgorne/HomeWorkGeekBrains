using System;


namespace Homework_GB_2
{
    internal class Program
    {
        static void Main()
        {
            Console.WriteLine($"Укажите, пожалуйста, номер задачи от 1 до 3х: ");
            int n;
            int.TryParse(Console.ReadLine(), out n);
            switch (n)
            {
                case 1:
                    Console.WriteLine("Вывод второго числа, задача N10");
                    Print_twoNumbs();//10_Print_twoNumbs
                    break;
                case 2:
                    Console.WriteLine("Вывод третьего числа, задача N13");
                    Print_threeNumbs();//13_Print_threeNumbs
                    break;
                case 3:
                    Console.WriteLine("Проверка дня недели, задача N10");
                    Print_Day_of_Week();//15_Day_of_Week
                    break;
                default:
                    Console.WriteLine("Введите номер задачи");
                    Main();
                    break;
            }

        }

        //15_Day_of_Week
        static void Print_Day_of_Week()
        { 
        Console.WriteLine("Введите цифру дня недели");
            int numbDay;
            int.TryParse(Console.ReadLine(), out numbDay);
            if (numbDay == 7 || numbDay == 6)
            {
                Console.WriteLine("Это выходной!");
            }
            else if (numbDay >= 1 && numbDay <= 7)
            {
                Console.WriteLine("Это рабочий день!");
            }
            else
            {
                Console.WriteLine("День не существует!");
            }
            Print_Day_of_Week();
        }

        //13_Print_threeNumbs
        static void Print_threeNumbs()
        {
            /*
            int n;
            Console.WriteLine("Введите число: ");
            var bools = int.TryParse(Console.ReadLine(), out n);
            if (bools == false)
            {
                Print_threeNumbs();
            }
            else if (bools == true)
            {
                int res = 0;
                if (n < 1000 && n > 100)
                {
                    n *= 10;
                }
                else if (n < 100)
                {
                    Console.WriteLine("Третьей цифры нет");
                    Print_threeNumbs();
                }
                while (n > 1000)
                {
                    n /= 10;
                    if (n <= 9999)
                    {
                        res = n % 10;
                    }
                }
                Console.WriteLine(res);
            }
            */
            
            //OR THAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            Console.Write("Введите число: ");

            int numb;
            var tryS = int.TryParse(Console.ReadLine(), out numb);
            if (tryS == true)
            {
                string numbToStr = Convert.ToString(numb);
                if (numbToStr.Length > 2)
                {
                    Console.WriteLine("Третья цифра: " + numbToStr[2]);
                }
                else
                {
                    Console.WriteLine("Третьей цифры нет");
                    Print_threeNumbs();
                }
            }
            else
                Print_threeNumbs();
            

        }
        //10_Print_twoNumbs 
        static void Print_twoNumbs()
        {     
            int n;
            Console.WriteLine("Введите число: ");
            int.TryParse(Console.ReadLine(), out n);

            if(n > 999 || n < 100)
            {
                Console.WriteLine("Введите трехзначное число: ");
                Print_twoNumbs();
            }

            if (n <= 999)
            {
                int z = (n / 10) % 10;
                Console.WriteLine(z);
            }
        }
    }
}
