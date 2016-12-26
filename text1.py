while 1:
    def fib(x):
        n, a, b = 0, 0, 1
        while n < x:
            print b
            a, b = b, a + b
            n = n + 1
    x = int(raw_input('input x:'))
    fib(x)