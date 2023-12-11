income = int(input('Enter your income: '))

threshold_one = income * 0.00
threshold_two = income * 0.10
threshold_three = threshold_two + (income - 20000) * 0.20

if income in range(10001, 20000):
    print(f'Your income tax rate is {threshold_two}.')
elif income > 20000:
    print(f'Your income tax rate is {threshold_three}')
else:
    print(f'Your income tax rate is {threshold_one}.')
