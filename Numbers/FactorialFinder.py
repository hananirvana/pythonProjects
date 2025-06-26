"""
Factorial Finder - The Factorial of a positive integer, n, is defined as the product
of the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1.
Solve this using both loops and recursion.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
