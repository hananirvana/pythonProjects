"""
Find e to the Nth Digit - Just like the previous problem,
but with e instead of π (pi). Enter a number and have
the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math

def e_to_nth(digit):
    if digit >= 100:
        return "Exceeded limit."
    return round(math.e, digit)

print(e_to_nth(5))
