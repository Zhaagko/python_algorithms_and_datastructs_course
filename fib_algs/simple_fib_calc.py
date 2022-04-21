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

# tests
# print(fib(3))
# print(fib(5))
print(fib(20))
