def fib(n):
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


for i in range (1000000):

   print(fib(i))
