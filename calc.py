import math

# --- New functions (placed above add as instructed) ---

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        raise ValueError(e)


def hypotenuse(a, b):
    # math.hypot handles negatives correctly
    return math.hypot(a, b)


# --- Core calculator functions ---

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# alias for merge requirement
def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


# alias for merge requirement
def mul(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


# alias for merge requirement
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    try:
        if a <= 0 or a == 1:
            raise ValueError("Log base must be positive and not equal to 1.")
        if b <= 0:
            raise ValueError("Log argument must be positive.")
        return math.log(b, a)
    except ValueError as e:
        raise ValueError(e)


def exponent(a, b):
    return a ** b


# alias for merge requirement
def exp(a, b):
    return a ** b


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def log(a, b):
    # log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Log argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a ** b
