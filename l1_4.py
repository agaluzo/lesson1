MinFixedMonthlyPayment = 10
balance = 3926
annualInterestRate = 0.2
unpaidBalance = updatedBalance = balance
totalPaid = 0

while True:
    for i in range (1, 13):
        unpaidBalance = updatedBalance - MinFixedMonthlyPayment
        interest = annualInterestRate/12 * unpaidBalance
        updatedBalance = unpaidBalance + interest
    if unpaidBalance > 0:
        updatedBalance = balance
        MinFixedMonthlyPayment += 10
    else:
        break

print('Lowest payment: %d' % MinFixedMonthlyPayment)


jk
