"""
Prime Factorization - Have the user enter a
number and find all Prime Factors
(if there are any) and display them.
"""
import math

def prime_factorize(n):
    ls = []
    while n % 2 == 0:
        ls.append(2)
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            ls.append(i)
            n = n / i
    if n > 2:
        ls.append(n)
    return ls

print(prime_factorize(597))




