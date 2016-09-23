balance = int(input('Enter valid balance: '))
annualInterestRate = float(input('Enter valid  annual interest rate: '))
monthlyPaymentRate = float(input('Enter valid  minimum monthly payment rate: '))
totalPaid = 0

for i in range (1, 13):
    minMonthlyPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minMonthlyPayment
    interest = annualInterestRate/12 * unpaidBalance
    balance = unpaidBalance + interest
    totalPaid += minMonthlyPayment
    print('Month %s' % i)
    print('Minimum monthly payment: %.2f' % minMonthlyPayment)
    print('Remaining balance: %.2f' % balance)

print('Total paid:  %.2f' % totalPaid)
print('Remaining balance: %.2f' % balance)