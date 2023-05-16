class Fibonacci:
    def __init__(self, limit):
        self.__limit = limit
        self.__index = 0
        self.__fib1 = self.__fib2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1

        if self.__index > self.__limit:
            raise StopIteration

        if self.__index in [1, 2]:
            return 1

        auxiliary = self.__fib1 + self.__fib2
        self.__fib1, self.__fib2 = self.__fib2, auxiliary

        return auxiliary


class Class:
    def __init__(self, limit):
        self.__iter = Fibonacci(limit)

    def __iter__(self):
        return self.__iter


for i in Fibonacci(10):
    print(i)

my_fibonacci = Class(8)

for i in my_fibonacci:
    print(i)