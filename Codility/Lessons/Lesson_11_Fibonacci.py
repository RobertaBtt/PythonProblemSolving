
class Fibonacci:
    def fibonacci(n):
        if (n <= 1):
            return n
        return Fibonacci.fibonacci(n - 1) + Fibonacci.fibonacci(n - 2)


    def fibonacciDynamic(n):
        fib = [0] * (n-1)
        fib[1] = 1


        for i in range(2, n -1):
            fib[i] = fib[i - 1] + fib[i - 2]
            sum = fib[i]
            if sum > n:
                return fib[:i]


#print(Fibonacci.fibonacci(4))
print(Fibonacci.fibonacciDynamic(9))
print(Fibonacci.fibonacciDynamic(56))
print(Fibonacci.fibonacciDynamic(89))
print(Fibonacci.fibonacciDynamic(146))