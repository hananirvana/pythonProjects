def complex_add(z1, z2):
    # Addition of two complex numbers
    return z1 + z2

def complex_multiply(z1, z2):
    # Multiplication of two complex numbers
    return z1 * z2

def complex_negate(z):
    # Negation of a complex number
    return -z

def complex_invert(z):
    # Inversion of a complex number
    conjugate = z.conjugate()
    squared_mag = z.real**2 + z.imag**2
    return conjugate / squared_mag


z1 = 3 + 4j
z2 = 1 - 2j

result_addition = complex_add(z1, z2)
print("Addition:", result_addition)
