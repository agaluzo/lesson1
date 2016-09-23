MinFixedMonthlyPayment = 10
balance = int(input('Enter valid balance: '))
annualInterestRate = float(input('Enter valid  annual interest rate: '))
updatedBalance = balance

while True:
    for i in range (0, 12):
        unpaidBalance = updatedBalance - MinFixedMonthlyPayment
        interest = annualInterestRate/12 * unpaidBalance
        updatedBalance = unpaidBalance + interest
    if unpaidBalance > 0:
        updatedBalance = balance
        MinFixedMonthlyPayment += 10
    else:
        break

print('Lowest payment: %d' % MinFixedMonthlyPayment)