"""
Unit Converter (temp, currency, volume, mass and more) -
Converts various units between one another. The user enters
the type of unit being entered, the type of unit they want
to convert to and then the value. The program will then make
the conversion.
This is a work in progress, expect this to be finished later.
"""
from forex_python.converter import CurrencyRates

def temp_convert(temp,deg):
    if deg == "F":
        return (temp-32) * 5/9
    elif deg == "C":
        return (temp*9/5) + 32
    else:
        return None

def currency(cc,money,tc):
    cc.upper()
    tc.upper()
    return c.convert(cc, tc, money)

def volume(obj):
    pass

