import math


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2


def mod(num1, num2):
    return num1 % num2


def sqrt(num1):
    return math.sqrt(num1)


def square(num1):
    return num1 ** 2


def cube(num1):
    return num1 ** 3


def factorial(num1):
    return math.factorial(num1)


def fibonacci(num1):
    return math.fib(num1)


if __name__ == '__main__':
    modulo = mod(6, 2)
    print(modulo)