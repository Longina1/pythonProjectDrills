def name_and_age(name, age):
    print('The name is:', name, 'and the age is:', age)

name_and_age("Nina", 30)

def func1(*args):
    for argument in args:
        print(argument)

func1(20, 40, 60)

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    res = f'{a} added to {b} is equal to {addition} and {b} subtracted from {a} equals to {subtraction}.'
    return res

res = calculation(40, 10)
print(res)

def showEmployee(name, salary=9000):
    employee = f'Name: {name}, salary: {salary}'
    return employee

print(showEmployee('Ben'))


for number in range(4,30):
    if number % 2 == 0:
        list = []
        list.append(number)
        print(list)


x = [4, 6, 8, 24, 12, 2]
print(max(x))
