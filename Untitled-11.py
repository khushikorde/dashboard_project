def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Calculate factorial
num = 5
print(f"Factorial of {num}: {math_utils.factorial(num)}")

# Calculate GCD
a = 12
b = 15
print(f"GCD of {a} and {b}: {math_utils.gcd(a, b)}")

# Calculate LCM
print(f"LCM of {a} and {b}: {math_utils.lcm(a, b)}")

# Check if a number is prime
num = 23
print(f"Is {num} prime? {math_utils.is_prime(num)}")


