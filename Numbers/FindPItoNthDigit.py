"""
Find PI to the Nth Digit - Enter a number and have
the program generate π (pi) up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math

def pi_to_nth(digit):
    if digit >= 100:
        return "Exceeded Limit."

    return round(math.pi, digit)

print(pi_to_nth(5))
