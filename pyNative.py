number = input('Enter a number: ')
reversed_number = str(number)[::-1]
print(reversed_number, end=" ")

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
