def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a
def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a