"""
Calculator - A simple calculator to do basic operators.
6 Basic Operations ------------------------------------
Square Root: (√)
Division: (/)
Percentage: (%)
Multiplication: (*)
Subtraction: (-)
Addition: (+)
"""
from math import sqrt


def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


def percentage(n1, n2):
    return (n1 / 100) * n2


def square_root(n1):
    return sqrt(n1)


if __name__ == '__main__':
    res = input(
        "What would you like to do? \na-addition \ns-subtraction \nd-division \nm-multiplication \nsq-square root \np-percentage \n")

    if res == "a":
        n1 = int(input())
        n2 = int(input())
        print(addition(n1, n2))
    elif res == "s":
        n1 = int(input())
        n2 = int(input())
        print(subtraction(n1, n2))
    elif res == "d":
        n1 = int(input())
        n2 = int(input())
        print(division(n1, n2))
    elif res == "m":
        n1 = int(input())
        n2 = int(input())
        print(multiplication(n1, n2))
    elif res == "sq":
        n1 = int(input())
        print(square_root(n1))
    elif res == "p":
        n1 = int(input())
        n2 = int(input())
        print(percentage(n1, n2))
    else:
        print("Sorry, incorrect option. Reload to retype option.")
