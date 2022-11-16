using System;


namespace GB_3
{
    class Program
    {
        public static void Main(string[] args)
        {
            Cube_Numbers();//23_Cube_Numbers
            Coordinates_Delta();//21_Coordinates_Delta
            TryIsPalindrom();//19_Try_Palindrom
        }

        //23_Cube_Numbers
        static void Cube_Numbers()
        {
            int numb;
            int i = 1;

            Console.WriteLine("Нахождение куба числа \n Введите число: ");
            int.TryParse(Console.ReadLine(), out numb);
            while(i <= numb)
            {
                Console.WriteLine($"Куб числа {i}: \n {Math.Pow(i, 3)}");
                i++;   
            } 
        }

        //21_Coordinates_Delta
        static void Coordinates_Delta()
        {
            //по хорошему лучше было бы создать класс Point, создать экземпляр класса
            //new Point(), в ctor(конструкторе) задать значения и закинуть формулу для вычисления
            

            char Numb_Coordinate;
            double x1, y1, x2, y2, z1, z2, delta;

            Console.Write("Расстояние между точками \n Нажмите Enter и введите координаты");
            char.TryParse(Console.ReadLine(), out Numb_Coordinate);

                    Console.WriteLine("Введите координаты A(x): ");
                    x1 = Convert.ToDouble(Console.ReadLine());
                
                    Console.WriteLine("Введите координаты A(y): ");
                    y1 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine("Введите координаты A(z): ");
                    z1 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine("Введите координаты B(x): ");
                    x2 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine("Введите координаты B(y): ");
                    y2 = Convert.ToDouble(Console.ReadLine());

                    Console.WriteLine("Введите координаты B(z): ");
                    z2 = Convert.ToDouble(Console.ReadLine());
 
            delta = Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2) + Math.Pow(z2 - z1, 2));
            Console.WriteLine($"Дистанция между точками равна: {Math.Round(delta, 2)}");
        }

        //19_Try_Palindrom
        static void TryIsPalindrom()
        {
            start_Try:
            int number;
            Console.WriteLine("Проверка числа на палиндром \n Введите число для проверки/");
            int.TryParse(Console.ReadLine(), out number);

            int oldValue = number;
            int newValue = 0;
            while (number > 0)
            {
                int dig = number % 10;
                newValue = newValue * 10 + dig;
                number = number / 10;
            }
            if (newValue == oldValue)
                Console.WriteLine("Число является палиндромом");
            else
                Console.WriteLine("Число не является палиндромом");
            goto start_Try;
        }
    }
}
