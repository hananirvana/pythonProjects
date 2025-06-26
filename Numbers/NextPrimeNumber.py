"""
Next Prime Number - Have the program find
prime numbers until the user chooses to
stop asking for the next one.
"""
import math


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def get_next_prime(num):
    j = num + 1
    while True:
        if is_prime(j):
            return j
        j += 1

if __name__ == "__main__":
    print("Press enter to continue, d to stop")

    n = 2
    while True:
        print(n)
        user_input = input("Done? ")
        if user_input == 'd':
            print("done.")
            break
        n = get_next_prime(n)
