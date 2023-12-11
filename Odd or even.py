n = int(input('Input your number: '))
mod = n % 4
if mod == 0:
    print('Your number is even and is a multiple of 4.')
elif mod == 0:
    print('Your number is even.')
else:
    print('Your number is odd.')


num = int(input('Enter a number to check: '))
check = int(input('Enter a number to divide by: '))
mod = num % check
if mod == 0:
    print('Your number can be evenly divided by the check number.')
else:
    print('Your number cannot be evenly divided by the check number.')
