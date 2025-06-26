"""
Fast Exponentiation - Ask the user to enter 2 integers a and b and output a^b
(i.e. pow(a,b)) in O(lg n) time complexity.  (DONE)

WARNING: Do not put a big number as an exponent; if the code doesn't respond when run, terminate.
"""

import timeit

start = '''
f1(100)
'''
setup = '''
def f1(a):
    return a**10
'''
print('Time for function1: ', timeit.timeit(start,setup,number=1000000))

start = '''
f2(100)
'''
setup = '''
def f2(a):
    return pow(a,10)
'''
print('Time for function2', timeit.timeit(start,setup,number=1000000))

