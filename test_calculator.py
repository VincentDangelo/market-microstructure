import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def sub(a, b):
    return subtract(a, b)


def multiply(a, b):
    return a * b


def mul(a, b):
    return multiply(a, b)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def div(a, b):
    return divide(a, b)


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Log argument must be positive.")
    return math.log(b, a)


def log(a, b):
    return logarithm(a, b)


def exponent(a, b):
    return a ** b


def exp(a, b):
    return a ** b
