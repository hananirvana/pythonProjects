"""
Number Names - Show how to spell out a number in English. You can use a
preexisting implementation or roll your own, but you should support inputs up to at
least one million (or the maximum value of your language's default bounded integer type,
if that's less). Optional: Support for inputs other than positive integers (like zero,
negative integers, and floating-point numbers).
"""
import number_names

def num_name(num):
    return number_names.name(num)

print(num_name(1024345))
