num = str(input('Enter a number: '))
reversed_num = str((num)[::-1])
if num == reversed_num:
    print('The given number is a palindrome number.')
else:
    print('The given number is not a palindrome number.')
