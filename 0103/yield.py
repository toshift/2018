def fib_func(x):
    """
    フィボナッチ数列
    """
    a, b = 0, 1
    for _ in range(x):
        yield a
        a, b = b, (a+b)

if __name__ == "__main__":
    x = 100
    fib_num = fib_func(x)
    for gen in fib_num:
        print(gen)
