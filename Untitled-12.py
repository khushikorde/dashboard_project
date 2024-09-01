def fibonacci_iterative(n):
    """Calculate Fibonacci sequence up to the nth number using an iterative approach."""
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def fibonacci_recursive(n, a=0, b=1, fib_sequence=None):
    """Calculate Fibonacci sequence up to the nth number using a recursive approach."""
    if fib_sequence is None:
        fib_sequence = [0]

    if a > n:
        return fib_sequence

    fib_sequence.append(a)
    return fibonacci_recursive(n, b, a + b, fib_sequence)

# Example usage:
number = 50

# Using the iterative approach
iterative_result = fibonacci_iterative(number)
print(f"Fibonacci sequence up to {number} (Iterative): {iterative_result}")

# Using the recursive approach
recursive_result = fibonacci_recursive(number)
print(f"Fibonacci sequence up to {number} (Recursive): {recursive_result}")