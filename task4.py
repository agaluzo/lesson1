def findBalance ( balance, payment, annualInterestRate):
    for i in range(0, 12):
        unpaidBalance =  balance - payment
        interest = annualInterestRate / 12 * unpaidBalance
        balance = unpaidBalance + interest
    return balance

balance = int(input('Enter valid balance: '))
annualInterestRate = float(input('Enter valid  annual interest rate: '))
lowerBound = balance/12
upperBound = (balance * (1 + (annualInterestRate/12.0))**12) / 12
middle = lowerBound + (upperBound - lowerBound) / 2

while upperBound - lowerBound > 0.01:
    if findBalance(balance, middle, annualInterestRate)  > 0:
        lowerBound = middle
    elif findBalance(balance, middle, annualInterestRate)  < 0:
        upperBound = middle
    elif findBalance(balance, lowerBound, annualInterestRate) == 0:
        middle = lowerBound
        break
    elif findBalance(balance, upperBound, annualInterestRate) == 0:
        middle = upperBound
        break
    else:
        break
    middle = lowerBound + (upperBound - lowerBound) / 2

print('middle: %.2f' % (middle))


