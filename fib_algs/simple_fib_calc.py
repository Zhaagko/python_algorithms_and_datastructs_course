def fib(n):
    """Алгоритм возвращает n-е число Фибоначчи"""
    if n == 1 or n == 2:
        return 1

    x1, x2, xn = 1, 1, 0

    for i in range(n-2):
        xn = x1 + x2
        x1 = x2
        x2 = xn

    return xn

def fib_digit(n):
    """Алгоритм возвращает последний знак n-го числа Фибоначчи"""
    if n == 1 or n == 2:
        return 1

    x1, x2, xn = 1, 1, 0

    for i in range(n-2):
        xn = (x1 + x2) % 10
        x1 = x2 % 10
        x2 = xn % 10

    return xn
