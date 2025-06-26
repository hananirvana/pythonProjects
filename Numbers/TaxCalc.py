"""
Tax Calculator - Asks the user to enter a cost and either a country or state tax. It
then returns the tax plus the total cost with tax.
"""

def tax(cost, tx):
    return ((tx/100) * cost) + cost

print(tax(250, 6.0))
