num1 = 20
num2 = 30
product = int(num1 * num2)
sum = int(num1 + num2)

if product <= 1000:
    print(product)
else:
    print(sum)

num1 = 40
num2 = 30
product = int(num1 * num2)
sum = int(num1 + num2)

if product <= 1000:
    print(product)
else:
    print(sum)


numbers = str(input('Enter two numbers: '))
list_of_numbers = numbers.split()
x = int(list_of_numbers[0])
y = int(list_of_numbers[1])
def multiply(x, y):
    return x * y


print(f'{x} multiplied by {y} is {multiply(x, y)}')