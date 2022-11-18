# 3. Создайте программу для игры в ""Крестики-нолики"".

from colorama import init, Fore, Back, Style 

board = list(range(1,30))
# Initializes Colorama # Для интереса решил попробовать библиотеку с цветами
init(autoreset=True) 
def draw_board(board):
   print((Style.BRIGHT + Back.GREEN + Fore.RED + "-" )* 13)
   for i in range(3):
        print(Style.BRIGHT + Back.GREEN + Fore.RED +  "|", 
        board[0+i*3], Style.BRIGHT + Back.GREEN + Fore.RED +  "|", 
        board[1+i*3],Style.BRIGHT + Back.GREEN + Fore.RED + "|", board[2+i*3],Style.BRIGHT + Back.GREEN + Fore.RED + "|")
        print((Style.BRIGHT + Back.GREEN + Fore.RED + "-" )* 13)
#draw_board(board)# Проверка доски


def inputs(item):
   Tryes = False
   while not Tryes:
      choice = input("Выберите ячейку " + item+"? ")
      try:
         choice = int(choice)
      except:
         print("Введите номер ячейки")
         continue
      if choice >= 1 and choice <= 9:
         if(str(board[choice-1]) not in "XO"):
            board[choice-1] = item
            Tryes = True
         else:
            print("Выберите незанятую клетку")
      else:
        print("Введите номер ячейки от 1 до 9.")

def check_matrix(board):
   board_matrix = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for vart in board_matrix:
       if board[vart[0]] == board[vart[1]] == board[vart[2]]:
          return board[vart[0]]
   return False

def main(board):
    n = 0
    win = False
    while not win:
        draw_board(board)
        if n % 2 == 0:
           inputs("X")
        else:
           inputs("O")
        n += 1
        if n > 4:
           tmp = check_matrix(board)
           if tmp:
              print(tmp, "Win")
              win = True
              break
        if n == 9:
            print("Draw")
            break
    draw_board(board)
main(board)