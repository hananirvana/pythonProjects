def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


prime_num = list(filter(is_prime, range(1, 100)))

print(prime_num)


