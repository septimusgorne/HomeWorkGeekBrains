def calc(a, s, b):
    while True:
        s = input("(+, -, *, /)")
        if s == 'exit':
            break
        if s in ('+', '*', '-', '/'):
            a = float(input())
            y = float(input())
        if s == '+':
            value = a + b
        elif s == '*':
            value = a * b
        elif s == '/' and b !=0:
            value = a / b
        elif s == '/' and b == 0:
            print("На ноль делить нельзя!")
    else:
        print("Введите корректный знак")
    return value
calc(input(), input(), input())