//Более сложный вариант без стандартных функций
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
            Unique_Arr(numb);
        }
        private static void Unique_Arr(int numb)
        {
            int[] myArray = new int[numb];
            int x = 0;
            for (int i = 0; i < myArray.Length; i++)
            {
                Console.Write($"Введите элемент индекса {i}: \t"); ;
                myArray[i] = int.Parse(Console.ReadLine());
            }

            var notUniqEl = 0;//считаем повторяющиеся элементы
            for (int i = 1; i < myArray.Length; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    if (myArray[i] == myArray[j]) //проверяем на уникальность
                    {
                        notUniqEl++;     //Если элемент повторился, добавляем, по циклу идём к следующему элементу
                    }
                }
            }

            int[] uniqueArray = new int[myArray.Length - notUniqEl]; // Создаем массив уникальных элементов(из него вычитаем повторяющиеся)
            uniqueArray[0] = myArray[0];   //Записываем первый элемент( так как выводим по заданию с первого уникального элемента, первый уже уникальный) 
            for (int i = 1, index = 1; i < myArray.Length; i++)
            {
                var uniqueElement = true;   //Для проверки уникальности присваиваем true
                for (int j = 0; j < i; j++)
                {
                    if (myArray[i] == myArray[j])//Проверяем уникальность для записи в новый массив
                    {
                        uniqueElement = false;
                        break;//Пропускаем если элемент повторяется
                    }
                }
                if (uniqueElement)//Если уникальный
                {
                    uniqueArray[index] = myArray[i];// Записываем уникальный элемент в массив
                    index++; //Индекс для записи в массив уникальных чисел
                }
            }
            foreach (var el in uniqueArray)
            {
                Console.WriteLine(el);
            }

            Console.ReadKey();
        }
    }
}
