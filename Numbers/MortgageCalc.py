"""
Mortgage Calculator - Calculate the monthly payments
of a fixed term mortgage over given Nth terms at a given
interest rate. Also figure out how long it will take the
user to pay back the loan. For added complexity, add an
option for users to select the compounding interval
(Monthly, Weekly, Daily, Continually).
"""
def monthly_mortage(loan, interest, term):
    p = loan
    r = interest
    n = 12
    t = term
    y = -abs(n)
    return (p*(r/n))/(1-(1+r/n)**(y*t))


print(monthly_mortage(400000,0.05,30))
