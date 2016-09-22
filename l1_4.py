balance = 320000
annualInterestRate = 0.2
lowerBound = balance/12
upperBound = (balance * (1 + (annualInterestRate/12.0))**12) / 12

def findBalance (balance, payment, annualInterestRate):
    for i in range(1, 13):
        unpaidBalance = balance - payment
        interest = annualInterestRate / 12 * unpaidBalance
        balance = unpaidBalance + interest
    return balance

while upperBound - lowerBound > 0.01:
    middle = lowerBound + (upperBound - lowerBound) / 2
    if findBalance(balance, lowerBound, annualInterestRate) * (findBalance(balance, middle, annualInterestRate)) < 0 :
        upperBound = middle
    elif findBalance(balance, upperBound, annualInterestRate) * (findBalance(balance, middle, annualInterestRate)) < 0 :
        lowerBound = middle
    else:
        break

print('middle: %.2f' % (middle))
