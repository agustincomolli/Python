def fibonacci(limit):
    fib1 = fib2 = 1
    for i in range(limit):
        if i in [0,1]:
            yield 1
        else:
            auxiliary = fib1 + fib2
            fib1, fib2 = fib2, auxiliary
            yield auxiliary


fibonacci_numbers = list(fibonacci(10))
print(fibonacci_numbers)