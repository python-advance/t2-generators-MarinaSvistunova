'''
Инвариантная самостоятельная работа

2.1. На основе кода, предоставленного преподавателем, реализовать генератор чисел ряда Фибоначчи.
     Генератор требуется создать двумя вариантами: с помощью генератора списков, с помощью функции,
     внутри которой yield.

'''

def fib(n):
    value = 1
    if n == 0:
        value = 0
    if n > 2:
        value = fib(n - 1) + fib(n - 2)
    return value


def fib_yield(n):
    a, b = 1, 1

    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':

    # генератор списков
    n = 20
    gen_list = [fib(i) for i in range(n + 1)]
    print(gen_list)

    # с помощью функции, внутри которой yield.
    fib_func_yield = fib_yield(n)
    for i in range(n):
        print(fib_func_yield.__next__())
