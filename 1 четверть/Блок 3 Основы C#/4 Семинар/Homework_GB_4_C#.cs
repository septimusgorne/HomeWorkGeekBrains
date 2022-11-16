using System;

namespace GB_4
{
    class Program
    {
        public static void Main(string[] args)
        {
            Pow();//Задача 25, возведение числа в степень
            Sum_Numbers();//Задача 27, сумма цифр, цикл
            Print_Array();//Задача 29, ввод-вывод массива
        }

        //("Задача 25, возведение числа в степень");
        static void Pow()
        {
            int num1, num2;
            int res = 1;
            Console.WriteLine("Введите число возводимое в степень: ");
            int.TryParse(Console.ReadLine(), out num1);
            Console.WriteLine("Введите степень");
            int.TryParse(Console.ReadLine(), out num2);

            for (int i = 1; i <= num2; i++)
            {
                res = res * num1;
            }
            Console.WriteLine($"Результат: {res}");
            Pow();
        }

        //("Задача 27, сумма цифр");
        static void Sum_Numbers()
        {
            int num;
            int res = 0;

            Console.WriteLine("Введите число");
            int.TryParse(Console.ReadLine(), out num);

            while(num > 0)
            {
                res += num % 10;
                num = num / 10;
            }
            Console.WriteLine(res);
        }

        //("Задача 29, ввод-вывод массива");
        static void Print_Array()
        {
            Console.WriteLine("Введите количество элементов массива");
            int el;
            int.TryParse(Console.ReadLine(), out el);

            int[] arr= new int[el];
            for (int i = 0; i < el; i++)
            {
                Console.WriteLine($"Введите {i} элемент " + "\t");
                arr[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.WriteLine($"Элементы массива из {el} элементов");
            foreach (var item in arr)
            {
                Console.Write(" " + item);
            }
        }
    }
}