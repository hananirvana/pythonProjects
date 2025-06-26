"""
Fibonacci Sequence - Enter a number and have
the program generate the Fibonacci sequence
to that number or to the Nth number.
"""

def fibo_seq(limit):
    a = 1
    b = 1
    for i in range(limit):
        yield a
        a, b = b, a + b

ls = [x for x in fibo_seq(10)]  # i have to use an iterator because the result is an iterator obj.
print(ls)
